GREEN_COLOR = "\033[32m"
YELLOW_COLOR = "\033[33m"
RED_COLOR = "\033[31m"
firstAsciArt = "\033[95m" + '''
_____ _____ _   _ _  _______ ____  _____  _____  
|  __ \_   _| \ | | |/ / ____/ __ \|  __ \|  __ \ 
| |__) || | |  \| | ' / |   | |  | | |__) | |  | |
|  ___/ | | | . ` |  <| |   | |  | |  _  /| |  | |
| |    _| |_| |\  | . \ |___| |__| | | \ \| |__| |
|_|   |_____|_| \_|_|\_\_____\____/|_|  \_\_____/ 
'''
content = f'''
{RED_COLOR}[!] click to skip animations
{GREEN_COLOR}[*] what is pinkcord
{YELLOW_COLOR}[?] Pinkcord is an Remote Access Trojan (R.A.T) open source computer virus written in Python that utilizes Discord bots to transmit information.
{GREEN_COLOR}[*] how to download and use it?
{YELLOW_COLOR}[1] download files from github
[2] download python from official site
[3] run setup.bat or run setup.py manually via cmd
[4] run the generated exe file on computer
{RED_COLOR}[!] some functions may not work on linux, so I recommend using windows to run setup
{GREEN_COLOR}[*] inspiration
{YELLOW_COLOR}[?] meterpreter from metasploit
{GREEN_COLOR}[*] what pinkcord as a virus can do
{YELLOW_COLOR}[?] the virus can execute cmd commands, send files in two directions, the virus also has a built-in keylogger, it can make screens, steal cookies from the browser and much much more
{RED_COLOR}[!] more information about commands and technical information can be found on github
{GREEN_COLOR}[*] about the author
{YELLOW_COLOR}[?] I am a 17 year old programmer and ethical hacker pinkcord is my best project so far you can find more of my projects on github
{RED_COLOR}[!] hacking the world..... [!]
\033[0m[{GREEN_COLOR}====================\033[0m] {RED_COLOR} 100%
{GREEN_COLOR}[*] world hacked
[*] thanks for reading, enjoy using pinkcord
[*] if you liked the pinkcord project don't forget to give a star on github                        
'''
secondAsciArt = RED_COLOR + '''
______   _   _   _____  
|  ____| | \ | | |  __ \ 
| |__    |  \| | | |  | |
|  __|   | . ` | | |  | |
| |____ _| |\  |_| |__| |
|______(_)_| \_(_)_____/ 
'''
autor = RED_COLOR + "[author] xanonDev \033[0m"
print(firstAsciArt)
lines = content.split('\n')
import time
for line in lines:
    time.sleep(0.4)
    print(line)
print(secondAsciArt)
print(autor)
