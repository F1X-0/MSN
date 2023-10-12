from pyngrok import ngrok
from colored import fore, back
import datetime
import requests
import logging
import time
import json
import os

# ------- COLORS ------
light_blue  = fore(45)
white       = fore(255)
# ------- COLORS ------

# ------- MENU ------
menu = f'''{light_blue}
    
    █▀▄▀█ █ █▄░█ █▀▀ █▀▀ █▀█ ▄▀█ █▀▀ ▀█▀ ▄▄ █▀ █▀▀ █▀█ █░█ █▀▀ █▀█
    █░▀░█ █ █░▀█ ██▄ █▄▄ █▀▄ █▀█ █▀░ ░█░ ░░ ▄█ ██▄ █▀▄ ▀▄▀ ██▄ █▀▄

    █░█░█ █ ▀█▀ █░█   █▄░█ █▀▀ █▀█ █▀█ █▄▀
    ▀▄▀▄▀ █ ░█░ █▀█   █░▀█ █▄█ █▀▄ █▄█ █░█
{white}
'''
# ------- MENU ------

# ------- CONFIG ------
with open('config.json', 'r') as config:
    config = json.load(config)

global webhook, port, webhook_name, launch_delay
webhook         = config['webhook']
port 	        = config['port']
webhook_name    = config['webhook_name']
launch_delay    = config['launch_delay']

# ------- CONFIG ------

# ------- LOGGER ------
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[!] %(asctime)s - %(message)s'))
logger.addHandler(handler)
# ------- LOGGER ------

# ------- NGROK PROCESS ------
ngrok_process = ngrok.get_ngrok_process()
# ------- NGROK PROCESS ------

# ------- FUNCTIONS ------
def send_message(message, webhook):
    try:
        request = requests.post(webhook, json=message)
        request_srt = str(request)

        if request_srt == '<Response [204]>':
            print(f'    {light_blue}[*]{white} Sending webhook message')
        else:
            print(f'    {light_blue}[!]{white} Error sending webhook message')
    except:
        if webhook == '':
            print(f'    {light_blue}[!]{white} No webhook aviable')
        else:
            print(f'    {light_blue}[!]{white} Error with the webhook')


def start_tunnel():
    minecraft_tunnel = ngrok.connect(addr=port, proto='tcp')
    global minecraft_tunnel_url
    minecraft_tunnel_url = str(minecraft_tunnel)
    minecraft_tunnel_url = minecraft_tunnel_url.split()
    minecraft_tunnel_url = minecraft_tunnel_url[1].replace('"', '')
    minecraft_tunnel_url = minecraft_tunnel_url.replace('tcp://', '')


def send_tunnel():
    date = datetime.datetime.now()
    date = date.strftime("%H:%M:%S")

    message = {
      "username": f"{webhook_name}",
      "embeds": [
            {
                "title": "**--- SERVER STATUS ---**",
                "color": 31436,
                "fields":[
                    {
                        "name": f"**SERVER ADDRESS** : `{minecraft_tunnel_url}`",
                        "value": "",

                    },
                    {
                        "name": "**STATUS** : `OPEN`",
                        "value": "",

                    },
                    {
                        "name": f"**STARTED AT** : `{date}`",
                        "value": "",

                    },
                ],
                "footer": {
                    "text": "Made by : F1X-0",
                    "icon_url": "https://avatars.githubusercontent.com/u/76910908?v=4"
                }    
            }
        ]
    }

    send_message(message, webhook)


def main():
    try:
        print(f'    {light_blue}[*]{white} Launch delay {light_blue}:{white} {launch_delay}  ')
        time.sleep(launch_delay)
        start_tunnel()
        print(f'    {light_blue}[*]{white} Starting tunnel')
        print(f'    {light_blue}[*]{white} Ctrl + c to close the tunnel')
        print(f'    {light_blue}[*]{white} Server address {light_blue}:{white} {minecraft_tunnel_url}')
        send_tunnel()
        ngrok_process.proc.wait()
    except KeyboardInterrupt:
        print(f'    {light_blue}[*]{white} Closing server')
        ngrok.kill()

        date = datetime.datetime.now()
        date = date.strftime("%H:%M:%S")

        message = {
          "username": f"{webhook_name}",
          "embeds": [
                {
                    "title": "**--- TUNNEL STATUS ---**",
                    "color": 31436,
                    "fields":[
                        {
                            "name": "**STATUS** : `CLOSED`",
                            "value": "",

                        },
                        {
                            "name": f"**CLOSED AT** : `{date}`",
                            "value": "",

                        },
                    ],
                    "footer": {
                        "text": "Made by : F1X-0",
                        "icon_url": "https://avatars.githubusercontent.com/u/76910908?v=4"
                    }    
                }
            ]
        }
        send_message(message, webhook)
        print()
# ------- FUNCTIONS ------


if __name__ == '__main__':
    print(menu)
    main()
    