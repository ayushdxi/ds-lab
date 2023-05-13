import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 11101

msg = 'Hello from client'

s.sendto(msg.encode(), (host, port))

data, addr =  s.recvfrom(1024)

print(data.decode())