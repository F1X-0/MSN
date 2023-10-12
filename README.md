
# [ MSN ] Minecaft Server with Ngrok

Host your own Minecraft Server with Ngrok and share it through the Discord Webhook.


## Installation

- #### Clone it into a folder or Download the zip
    ```
    git clone https://github.com/F1X-0/MSN
    ```

- #### Go to the installation folder  and install the requirements

    ```
    pip install -r requirements.txt
    ```

## Usage/Examples
   
- #### Change the content of `config.json` :

    ```json
    {
        "webhook":"https://discord.com/api/webhooks/YourWebHookHere",
        "port":"25565",
        "webhook_name":"Minecaft Server with Ngrok",
        "launch_delay":10
    }
    ```

- #### Add the `server.jar` file into the folder
    - You can download it  [here](https://mcversions.net/)
    - You can check the official guide of how to setup the Minecraft Server [here](https://help.minecraft.net/hc/en-us/articles/360058525452-How-to-Setup-a-Minecraft-Java-Edition-Server)
    - Is recommended running the server manually once
    
        ```
        java -Xmx1024M -Xms1024M -jar .\server.jar --nogui
        ```
        
- #### Run the `start.bat` file to start the minecraft server and the Ngrok tunnel
## Screenshots
* #### The Ngrok Tunnel and Discord WebHook Manager

    ![App Screenshot](https://gcdnb.pbrd.co/images/q54x9ZrfBJg6.png)

* #### The Minecraft Server console
    ![App Screenshot](https://gcdnb.pbrd.co/images/JWYLKU38iAQI.png)

* #### The Discord WebHook Message
    ![App Screenshot](https://gcdnb.pbrd.co/images/Mdws1u83rmBU.png)
