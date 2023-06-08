# PINKCORD

Pinkcord is a computer virus written in Python that utilizes Discord bots to transmit information. Please note that this program was created solely for educational purposes, and it should not be used to engage in any illegal activities. The use of Pinkcord may have severe legal consequences, including the banning of your Discord account. Download and use this program responsibly.
to put it simply, pinkcord can be compared to meterpreter from metasploit
only pinkcord works outside the local network and transmits data via discord
and slightly different functions
![Banner](banner.jpg)

## How to Use

1. Install Python from the [official website](https://www.python.org/downloads/).
2. Download the files from this repository.
3. Open the command prompt in Windows or the terminal in Linux and run `python setup.py`. If that doesn't work, try `py setup.py`.
4. Follow the instructions provided.

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
- `!audio [session] [file_name]`: Plays an audio file.
- `!sessions`: Displays all sessions.
- `!rename [session] [new_name]`: Changes the name of a session.

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
- `playsound`: Playing sounds.
- `platform`: Recognizing the platform.

Please exercise caution and use this program responsibly. Remember that engaging in any illegal activities can result in serious consequences.
