![Banner](https://github.com/Jvr2022/pinkcord/blob/new-banner/pic/banner.png)

Pinkcord is a computer virus written in Python that utilizes Discord bots to transmit information. Please note that this program was created solely for educational purposes, and it should not be used to engage in any illegal activities. The use of Pinkcord may have severe legal consequences, including the banning of your Discord account. Download and use this program responsibly.
to put it simply, pinkcord can be compared to meterpreter from metasploit
only pinkcord works outside the local network and transmits data via discord
and slightly different functions

## How to Use

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Download the files from this repository.
3. Open a command prompt on Windows or a terminal on Linux and run python setup.py. If that doesn't work, try py setup.py. or if you are on windows you can just click on setup.bat
4. Follow the instructions provided.
5. if the program compiles to exe. just enable it on the computer you want to control

## Platforms
the program was written for windows, so a large amount may not work on normal linux, and even more so on termux or mac. it is possible that in the future there will be an adaptation of pinkcord to more platforms

## Commands

The following commands can be used with Pinkcord:

- `!shell [session] [output(yes, no)] [command]`: Executes a shell command on a remote computer.
- `!ss [session]`: Captures a screenshot from a remote computer.
- `!keylogger [session] [action(start, stop, log)]`: Starts or stops a keylogger on a remote computer.
- `!steal [session] [file_names]`: Steals files from a remote computer.
- `!info [session]`: Retrieves information about the remote computer system.
- `!cd [session] [path]`: Changes the current directory on the remote computer.
- `!up [session]`: Increases the volume on the remote computer.
- `!down [session]`: Decreases the volume on the remote computer.
- `!message [session] [title] [button] [message]`: Displays a message on the remote computer.
- `!dir [session]`: Displays the current directory on the remote computer.
- `!upload [session] [link] [file_name]`: Sends a file to the remote computer.
- `!click [session] [x] [y]`: Clicks at a specific location on the screen.
- `!press [session] [key]`: Presses a specific key (default: Enter).
- `!cli [session]`: Copies the clipboard content.
- `!write [session] [message]`: Types using the keyboard.
- `!loc [session]`: Displays IP information.
- `!cdrom [session]`: Opens the CD-ROM drive.
- `!sessions`: Displays all sessions.
- `!rename [session] [new_name]`: Changes the name of a session.
- `!startup [session] [file path]`: copy file to startup folder (you can copy pinkcord exe file)
- `!chrome [session] [action(cookie)]` - steals selected data from chrome
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



Please exercise caution and use this program responsibly. Remember that engaging in any illegal activities can result in serious consequences.
