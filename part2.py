#RSA
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
from Crypto.Cipher import PKCS1_OAEP

#part 2 w/ part 3

key = RSA.generate(2048)

#Alice - Sender
print('Hi Alice. What message would you like to send Bob?')
message = input()

cipher = PKCS1_OAEP.new(key)
cipherText = cipher.encrypt(message.encode())


print('Following is Alice\'s message encoded')
print('Cipher text:' , cipherText)


#Bob - Receiver
print('Bob has received the message and is now going to decrypt')
cipherToBob = PKCS1_OAEP.new(key)
messageToBob = cipherToBob.decrypt(cipherText)
print('Message:', messageToBob.decode())

