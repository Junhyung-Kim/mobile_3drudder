#!/usr/bin/env python3

import sys
import time
import platform
import rospy
import socket
from std_msgs.msg import Float32MultiArray

def talker():
    rospy.init_node('mobileInterface', anonymous=True)
    pub = rospy.Publisher('mobileCommand', Float32MultiArray, queue_size=1)

    aa = 2
    a = Float32MultiArray()
    a.data = [0.0, 0.0, 0.0, 0.0]

    ip = "127.0.0.1"
    port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip,port))
    server_socket.listen(0)
    client_socket, addr = server_socket.accept()
    print("socket waiting")
    i  = 5 
    while i>2:  
        data = client_socket.recv(65535)
        print(data)
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass