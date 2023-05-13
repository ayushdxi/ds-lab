import datetime
import socket
import time
s = socket.socket()
print("socket successfully created")
#server port 
port = 8011
s.bind(('',port))
s.listen(5)
print("Socket is listening...")
while True:
    connection, address = s.accept()
    connection.send(str(datetime.datetime.now()).encode())
		