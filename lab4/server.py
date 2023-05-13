import socket
import os
from _thread import *

#host, port
host = socket.gethostname()
port = 11106

#socket
s = socket.socket()
s.bind((host, port))

tc = 0

def cli_thread(conn):
    #conn.send(str.encode('welcome to server'))
    print(tc)
    while True:
        data = conn.recv(1024)
        #print(data.decode())
        decoded = data.decode()
        print(decoded)
        numbers = decoded.split(' ')
        #print(int(numbers))
        sendback = []
        sendstr = ''
        for num in numbers:
            res = int(num) + 1  
            # sendback.append(res)
            sendstr += str(res)
            sendstr += ' '
        conn.sendall(sendstr.encode())
    conn.close()

s.listen(5)


while True:
    conn, addr = s.accept()
    start_new_thread(cli_thread, (conn, ))
    tc += 1
    

conn.close()