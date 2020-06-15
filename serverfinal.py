# Project by Mr-Competent
import socket
# Download pycrypto module (pip install pycrypto)
#for encryption we're using RSA
from Crypto.PublicKey import RSA  
from Crypto.Cipher import PKCS1_OAEP

keyPair = RSA.generate(2048)  #Generating Public key and private key

with open('rsa_server', 'wb') as f:  #opening a file to store the private key
    f.write(keyPair.exportKey('PEM'))

with open('rsa_server.pub', 'wb') as f:  #opening a file to store the public key
    f.write(keyPair.publickey().exportKey())
f.close()

file_pub = open('rsa_server.pub','rb')   #Reading public key from file
rsa_Server_pub = file_pub.read()

def encryption(text):   #for encryption of text
    encryptedText = cipherRSA.encrypt(text)
    return encryptedText

privateKey = RSA.importKey(open('rsa_server').read())  #reading the private key for encryption
cipherRSA2 = PKCS1_OAEP.new(privateKey)

def decryption(encryptedText):  #for decryption of text
    plainText = cipherRSA2.decrypt(encryptedText)
    text=plainText.decode('utf-8')
    return text

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creating socket
sock.bind(('127.0.0.1', 8888))   #binding socket with localhost at particular port
sock.listen(1)   #listening for single client
conn, addr = sock.accept()   #accepting connection

conn.send(rsa_Server_pub)  #sending public key to client

client_pub = conn.recv(1024)  #receiving public key from client
key = client_pub.decode('utf-8')  #decoding the client public key 

client_pubkey = open('rsa_client_s.pub','wb')  #writing the public key of client to a file
client_pubkey = client_pubkey.write(key.encode('ascii'))

client_publicKey = RSA.importKey(open('rsa_client_s.pub').read())  #reading the public key of client
cipherRSA = PKCS1_OAEP.new(client_publicKey)  #using client public key to make cipher(for encrypting message sent to client)

while True:
    msg = conn.recv(1024)  #receiving encrypted message from client
    msg2 = decryption(msg)  #decrypting message from client
    if msg2.lower() == 'exit' or msg2 == '0' or msg2.lower() == 'bye':  #for exiting
        print("Client Disconnected.")
        break
    print("Client : ", msg2)

    reply = input("Enter your message : ")  #message to client
    reply1 = reply.encode('ascii')  #encoding message
    conn.send(encryption(reply1))  #sending encrypted message 
    if reply.lower() == 'exit' or reply == '0' or reply.lower() == 'bye':  #for exiting
        print("Disconnected by Me.")
        break

# Encrypting message with the public key of client so that only client can read the message
# You can use ngrok to port forward to send to a remote location (For this no changes will be required in this script)
# You'll start ngrok and send your public ip or url with port allocated by ngrok to the client
# Each side three file will be generated. one will contain the public key of other, public key of own and private key of own.

# Thanks for reading. 

# Project by Mr-Competent