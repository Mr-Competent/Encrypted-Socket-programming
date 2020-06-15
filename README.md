# Simple Encrypted-Socket-programming
  A Simple Encrypted Socket Programming in python3 with pycrypto module

## Install pycrypto module
  pip install pycrypto  (for windows)

  pip3 install pycrypto  (for linux)

### You can use ngrok to port forward if your client is at remote location 
 - Server :- Start ngrok on server side and it should run until client disconnects.
 - Client :- Take ip or url and port allocated by ngrok from server.
   - comment the line           soc.connect(('127.0.0.1',8888))  to    #soc.connect(('127.0.0.1',8888))
   - uncomment the line     #soc.connect(('ip or url of ngrok','port of ngrok'))  to   soc.connect(('ip or url of ngrok','port of ngrok')) 
   - use the ip or url and port allocated by ngrok
   
