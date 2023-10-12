@echo off
start java -Xmx1024M -Xms1024M -jar .\server.jar --nogui
start python.exe main.py