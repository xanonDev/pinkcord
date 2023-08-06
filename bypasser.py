import codecs 
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Util.Padding import pad, unpad

def encrypt_code_AES(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ciphertext).decode()

with open("to_bypass.txt", 'r') as f:
    kod = f.read()
kod = kod.encode('utf-8')
kod = base64.b64encode(kod)
kod = kod.decode('utf-8')
kod = codecs.decode(kod, 'rot13')
salt = get_random_bytes(32)
password = "pinkcord_IS_awansome"
key = PBKDF2(password.encode(), salt, dkLen=32, count=1000000)
kod = encrypt_code_AES(kod, key)
f.close()
with open("to_bypass.txt", 'w') as f:
    f.write(kod)
with open("AES_KEY.txt", "wb") as f:
    f.write(base64.b64encode(key))
print("[*] encoded")
