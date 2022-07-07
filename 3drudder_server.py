import sys
import time
import platform
import socket
import ast
import numpy as np

#from multiprocessing import shared_memory
ip = "127.0.0.1"
port = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip,port))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
i  = 5 
while i>2:  
    data = client_socket.recv(65535)
    stringdata = data.decode('utf-8')
    print(len(stringdata))
    stringdata_s = stringdata[1:len(stringdata)-2]
    print(stringdata_s)
    strings = stringdata_s.split(',')
    print(strings)
    strings_n = np.array(strings)
    res = strings_n.astype(np.float)
    print(res)
    
