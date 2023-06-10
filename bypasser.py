import codecs 
import base64

with open("to_bypass.txt", 'r') as f:
    kod = f.read()
kod = kod.encode('utf-8')
kod = base64.b64encode(kod)
kod = kod.decode('utf-8')
kod = codecs.decode(kod, 'rot13')
f.close()
with open("to_bypass.txt", 'w') as f:
    f.write(kod)
print("[*] encoded")
