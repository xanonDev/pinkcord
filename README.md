![Banner](https://github.com/xanonDev/pinkcord/blob/main/pic/banner.png)
[![Support](https://img.shields.io/badge/Support-Buy%20me%20a%20Coffee-yellow)](https://www.buymeacoffee.com/pinkcord)
[![GitHub Stars](https://img.shields.io/github/stars/xanonDev/pinkcord.svg?style=flat&label=Stars&color=yellow)](https://github.com/xanonDev/pinkcord)
[![License](https://img.shields.io/github/license/xanonDev/pinkcord.svg?style=flat&label=License)](https://github.com/xanonDev/pinkcord/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/xanonDev/pinkcord.svg?style=flat&label=Issues&color=red)](https://github.com/xanonDev/pinkcord/issues)
[![GitHub Forks](https://img.shields.io/github/forks/xanonDev/pinkcord.svg?style=flat&label=Forks&color=blue)](https://github.com/xanonDev/pinkcord)

Pinkcord is a computer virus written in Python that utilizes Discord bots to transmit information. Please note that this program was created solely for educational purposes, and it should not be used to engage in any illegal activities. The use of Pinkcord may have severe legal consequences, including the banning of your Discord account. Download and use this program responsibly.
to put it simply, pinkcord can be compared to meterpreter from metasploit
only pinkcord works outside the local network and transmits data via discord
and slightly different functions

[For more information and instructions, visit the XDA Developers forum thread](https://forum.xda-developers.com/t/pinkcord-hack-discord-bots.4622267/).

## How to Use

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Download the files from this repository.
3. Open a command prompt on Windows or a terminal on Linux and run python setup.py. If that doesn't work, try py setup.py. or if you are on windows you can just click on setup.bat
4. Follow the instructions provided.
5. if the program compiles to exe. just enable it on the computer you want to control

## Platforms
the program was written for windows, so a large amount may not work on normal linux, and even more so on termux or mac. it is possible that in the future there will be an adaptation of pinkcord to more platforms

## Versions
you can choose the versions at setup
- `pinkcord_minimal.py` - the minimal version, the hardest to detect, has only reverse shell functions
- `pinkcord_lite.py` - has everything that the minimum version has, but unlike it, it can upload files and steal them, it has the function of taking screenshots, it can be slightly more detected by antiviruses
- `pinkcord.py` - it has all the features but antiviruses often detect it
## Commands

The following commands can be used with Pinkcord:

- `!shell [session] [output(yes, no)] [command]`: Executes a shell command on a remote computer. `all versions`
- `!ss [session]`: Captures a screenshot from a remote computer. `pinkcord.py and pinkcord lite`
- `!keylogger [session] [action(start, stop, log)]`: Starts or stops a keylogger on a remote computer. `only in pinkcord.py`
- `!steal [session] [file_names]`: Steals files from a remote computer. `pinkcord.py and pinkcord lite`
- `!info [session]`: Retrieves information about the remote computer system. `only in pinkcord.py`
- `!cd [session] [path]`: Changes the current directory on the remote computer. `all versions`
- `!up [session]`: Increases the volume on the remote computer. `only in pinkcord.py`
- `!down [session]`: Decreases the volume on the remote computer. `only in pinkcord.py`
- `!message [session] [title] [button] [message]`: Displays a message on the remote computer.`only in pinkcord.py`
- `!dir [session]`: Displays the current directory on the remote computer. `all versions`
- `!upload [session] [link] [file_name]`: Sends a file to the remote computer. `pinkcord.py and pinkcord lite`
- `!click [session] [x] [y]`: Clicks at a specific location on the screen. `only in pinkcord.py`
- `!press [session] [key]`: Presses a specific key (default: Enter). `only in pinkcord.py`
- `!cli [session]`: Copies the clipboard content. `only in pinkcord.py`
- `!write [session] [message]`: Types using the keyboard. `only in pinkcord.py`
- `!loc [session]`: Displays IP information. `only in pinkcord.py`
- `!cdrom [session]`: Opens the CD-ROM drive. `only in pinkcord.py`
- `!sessions`: Displays all sessions. `all versions`
- `!rename [session] [new_name]`: Changes the name of a session. `all versions`
- `!shutdown [session]`: Shuts down the remote computer. `all versions`
- `!startup [session] [file path]`: copy file to startup folder (you can copy pinkcord exe file) `only in pinkcord.py`
- `!restart [session]` - Restart the remote computer. `all versions`
- `!chrome [session] [action(cookie)]` - steals selected data from chrome `only in pinkcord.py`
- `!delete [session] [path]` - Deletes a file from the remote computer. `all versions`
- `!wallpaper [session] [path]` - changes the wallpaper on the remote computer. `only in pinkcord.py`
- `!kill [session] [task]` - remote task killing. `all versions`
- `!bsod [session]` - display bsod(blue screan of death). `only in pinkcord.py`
## Libraries Used

The following libraries are used in Pinkcord:

- `os`: Execution of system commands.
- `threading`: Launching a keylogger in another thread.
- `time`: Pausing the program for a specific duration using the sleep function.
- `zipfile`: Zipping data.
- `discord.py`: Communicating with Discord.
- `pyautogui`: Providing various functions related to user interface automation.
- `requests`: Communicating with other websites.
- `keyboard`: Operating the keyboard.
- `base64`: Encoding the token and program.
- `codecs`: Encoding the token and program.
- `sys`: Running Python commands.
- `pyperclip`: Stealing data from the clipboard.
- `subprocess`: Performing system functions.
- `platform`: Recognizing the platform.
- `shutil`: Copy files to startup.
- `sqlite3`: Opening a Chrome cookie file.
- `json`: Getting the decryption key.
- `win32crypt`: Decrypting cookies.
- `Cryptodome.Cipher`: Decrypting cookies.
- `ctypes`: change wallpaper and display bsod.

## Pinkcord Website

For more information, you can visit the [Pinkcord Project Website](https://pinkcord-project--xanondev.repl.co/) where you can find additional resources and details about the project.

---

Please exercise caution and use this program responsibly. Remember that engaging in any illegal activities can result in serious consequences.
