import socket
import time

host = socket.gethostname()
port = 11101

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))



while True:
    data, addr = s.recvfrom(1024)
    time = 'time is %s'%(time.ctime(time.time()))
    print('recv %s from %s'%(data.decode(), addr[0]))
    s.sendto(time.encode(), addr)