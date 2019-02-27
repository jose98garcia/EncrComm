import time

#-----------------------------------------
#HMAC with SHA256
from Crypto.Hash import HMAC, SHA256

#Alice - Sender
print('Enter a 7 byte message')
message = input()

while len(message) != 7:
    print('That is not a 7 byte message.. try again')
    message = input()

startH = time.time()

for x in range(100):
    h = HMAC.new(message.encode(), digestmod=SHA256)
    #print('Alice\'s message: ', message)
    #print('Alice\'s hashed message: ', h.hexdigest())

endH = time.time()
avgHMAC = (endH-startH)/100
print('Average HMAC Generation: ', avgHMAC)
'''
#Bob - Receiver
print('Bob has received the message and is now going to verify')

try:
    h.hexverify(h.hexdigest())
    print("Message '%s' is authentic" % message)

except ValueError:
    print('Message or key is wrong')
'''
#-----------------------------------------
#Digital Signature
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

key = RSA.generate(2048)

#Signature generation
print('Enter a 7 byte message')
message = input()

while len(message) != 7:
    print('That is not a 7 byte message.. try again')
    message = input()

startSig = time.time()

for x in range(100):
    h = SHA256.new(message.encode())
    sig = pkcs1_15.new(key).sign(h)

endSig = time.time()
avgSig = (endSig - startSig)/100
print('Signature Generation Time: ', avgSig)

#print('Message: ' , message)
#print('Signature: ', sig)

startVer = time.time()
#Signature verification
for x in range(100):
    pkcs1_15.new(key).verify(h,sig)
    #print('Signature is valid')

   

endVer = time.time()
avgVer = (endVer - startVer)/100
print('Signature Verification Time: ', avgVer)

