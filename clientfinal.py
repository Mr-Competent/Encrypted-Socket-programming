# Project by Mr-Competent
import socket
# Download pycrypto module (pip install pycrypto)
#for encryption we're using RSA
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP

keyPair = RSA.generate(2048) #generating public key and private key

with open('rsa_client', 'wb') as f:  #writing private key to a file
    f.write(keyPair.exportKey('PEM'))

with open('rsa_client.pub', 'wb') as f:  #writing public key to a file
    f.write(keyPair.publickey().exportKey())
f.close()

file_pub = open('rsa_client.pub','rb')  #reading public key 
rsa_me_pub = file_pub.read()

def encryption(text):    #encrypting text 
    encryptedText = cipherRSA.encrypt(text)
    return encryptedText

privateKey = RSA.importKey(open('rsa_client').read())  #reading private key
cipherRSA2 = PKCS1_OAEP.new(privateKey)  #for decrypting message sent by server

def decryption(encryptedText):   #for decryption 
    plainText = cipherRSA2.decrypt(encryptedText)
    text = plainText.decode('utf-8')
    return text

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating socket
soc.connect(('127.0.0.1',8888))   #connecting socket
# soc.connect(('ip or url of ngrok','port of ngrok'))   # To be used for remote location

Server_pub = soc.recv(1024)   #receiving public key from server
key = Server_pub.decode('utf-8')
server_pubkey = open('rsa_server_c.pub','wb')  #writing server public key to a file
server_pubkey = server_pubkey.write(key.encode('ascii'))
server_publicKey = RSA.importKey(open('rsa_server_c.pub').read())  #reading server public key 
cipherRSA = PKCS1_OAEP.new(server_publicKey)  #using server public key to make ciphers

soc.send(rsa_me_pub)  #sending own public key to server
while True:
    msg = input("Enter your message : ")  
    msg1 = msg.encode('ascii')
    soc.send(encryption(msg1))  #sending encrypting message
    if msg.lower() == 'exit' or msg == '0' or msg.lower() == 'bye':  #for exiting
        print("Disconnected by Me.")
        break

    reply = soc.recv(1024)  #receiving encrypted message
    msg2 = decryption(reply)  #decrypting message from server
    if msg2.lower() == 'exit' or msg2 == '0' or msg.lower() == 'bye':
        print("Disconnected by Server.")
        break

    print("Server : ",msg2)

# Encrypting with public key of server so that only server can read the message
# If server is using ngrok then you can easily receive the message 
# change soc.connect(('127.0.0.1',8888)) to soc.connect(('ip or url of ngrok','port of ngrok')) 
# Each side three file will be generated. one will contain the public key of other, public key of own and private key of own.

# Thanks for reading.

# Project by Mr-Competent
