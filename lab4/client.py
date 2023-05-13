import socket

s = socket.socket()

#host and port to connect
host = socket.gethostname()
port = 11106
s.connect((host, port))

while True:


    msg = input('integers separated by space: ')
    s.sendall(msg.encode())

    data = s.recv(1024)
    print(data)




