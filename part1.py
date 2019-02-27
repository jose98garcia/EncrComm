#AES
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
#-------------------------------------------
from base64 import b64decode
from Crypto.Util.Padding import unpad

#part1 w/ part 3

#Alice - Sender
print('Hi Alice. What message would you like to send Bob?')
message = input()
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv': iv, 'ciphertext' : ct})
print('Following is Alice\'s message encoded')
print(result)

#Bob - Receiver
print('Bob has received the message and is now going to decrypt')
b64 = json.loads(result)
iv = b64decode(b64['iv'])
ct = b64decode(b64['ciphertext'])
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)
print('Message from Alice: ', pt.decode('utf-8'))
