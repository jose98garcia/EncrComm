from Crypto.Hash import HMAC, SHA256

#Alice - Sender
print('Hi Alice. What message would you like to send Bob?')
message = input()
h = HMAC.new(message.encode(), digestmod=SHA256)
print('Alice\'s message: ', message)
print('Alice\'s hashed message: ', h.hexdigest())


#Bob - Receiver
print('Bob has received the message and is now going to verify')

try:
    h.hexverify(h.hexdigest())
    print("Message '%s' is authentic" % message)

except ValueError:
    print('Message or key is wrong')

