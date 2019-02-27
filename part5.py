from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

key = RSA.generate(2048)

#Alice - Sender
print('Hi Alice. What message would you like to send Bob?')
message = input()
h = SHA256.new(message.encode())

sig = pkcs1_15.new(key).sign(h)
print('Message: ' , message)
print('Signature: ', sig)

#Bob - Receiver
print('Bob has received the message and is now going to verify')
try:
    pkcs1_15.new(key).verify(h,sig)
    print('Signature is valid')

except ValueError:
    print('Signature is not valid')