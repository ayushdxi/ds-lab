import datetime
import time
import socket
# from dateutil import parser
from timeit import default_timer as timer

s = socket.socket()
port = 8011
s.connect(('127.0.0.1', port))
request_time = timer()
server_time = s.recv(1024).decode()
response_time = timer()
actual_time = datetime.datetime.now()
process_delay_latency = response_time - request_time
client_time = server_time + datetime.timedelta(seconds=process_delay_latency/2)
