# Tool made by Insur not skid please.

import requests
import string
import random
import time
import colorama
from colorama import Fore, Style

def ascii(text):
    gradient = ''
    colors = [Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        gradient += colors[i % len(colors)] + char
    return gradient + Style.RESET_ALL

def text(text):
    gradient = ''
    colors = [Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        gradient += colors[i % len(colors)] + char
    return gradient + Style.RESET_ALL

def send_mass_dm(Token, message):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json_data = {"content": message}
        time.sleep(1)
        r = requests.post(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
            headers=headers,
            json=json_data,
        )
        print(gradient_text(f"Sent DM To {channel['id']}"))

print(ascii("""
  _____                  _ _ 
 |  __ \                | | |
 | |  | |_ __ ___   __ _| | |
 | |  | | '_ ` _ \ / _` | | |
 | |__| | | | | | | (_| | | |
 |_____/|_| |_| |_|\__,_|_|_|
                    
         By @ InsurWeb
"""))

token = input(text("Enter A Token: "))
message = input(text("Enter the message to send: "))

send_mass_dm(token, message)
