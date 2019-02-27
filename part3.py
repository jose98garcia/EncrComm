import time

#AES
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.Padding import unpad

#Alice - Sender
print('Enter a 7 byte message')
message = input()

while len(message) != 7:
    print('That is not a 7 byte message.. try again')
    message = input()
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)


#time
startEncr = time.time()

#encryption for loop 
#print('Encrypting 100x')
for x in range(100):
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv': iv, 'ciphertext' : ct})
    #print('Following is Alice\'s message encoded')
    #print(result)

#how much time did AES Encrypt take
endEncr = time.time()
avgAesEncrypt = (endEncr - startEncr)/100
print('Avegerage AES Encryption Time: ', avgAesEncrypt)


#Bob - Receiver
#print('Bob has received the message and is now going to decrypt')
#print('Decrypting 100x')

startDecry = time.time()
for x in range(100):
    b64 = json.loads(result)
    iv = b64decode(b64['iv']) 
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = (cipher.decrypt(ct), AES.block_size)
    #print('Message from Alice: ', pt.decode('utf-8'))


#how much time did AES Decrypt take
endDecry = time.time()
avgAesDecrypt = (endDecry - startDecry)/100
print('Avegerage AES Decryption Time: ', avgAesDecrypt)





#---------------------------------------------------------------
#RSA
print('-----------------------------------------')
from base64 import b64decode
from Crypto.Util.Padding import unpad

from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

#Alice - Sender
print('Enter a 7 byte message')
message = input()

while len(message) != 7:
    print('That is not a 7 byte message.. try again')
    message = input()

rsaStart = time.time()
for x in range(100):
    cipher = PKCS1_OAEP.new(key)
    cipherText = cipher.encrypt(message.encode())
    #print('Following is Alice\'s message encoded')
    #print('Cipher text:' , cipherText)

rsaEnd = time.time()
avgRsaEncrypt = (rsaEnd - rsaStart)/100
print('Average RSA Encryption Time: ', avgRsaEncrypt)


rsaDStart = time.time()
#Bob - Receiver
#print('Bob has received the message and is now going to decrypt')
for x in range(100):
    cipherToBob = PKCS1_OAEP.new(key)
    messageToBob = cipherToBob.decrypt(cipherText)
    #print('Message:', messageToBob.decode())

rsaDEnd = time.time()
avgRsaDecrypt = (rsaDEnd - rsaDStart)/100
print('Average RSA Decryption Time: ', avgRsaDecrypt)

