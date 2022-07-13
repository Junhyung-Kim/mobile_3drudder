#!/usr/bin/env python3

import sys
import time
import platform
import rospy
import socket
import ast
import numpy as np
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

def talker():
    rospy.init_node('mobileInterface', anonymous=True)
    pub = rospy.Publisher('mobileCommand', Float32MultiArray, queue_size=1)
    pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


    aa = 2
    a = Float32MultiArray()
    a.data = [0.0, 0.0, 0.0, 0.0]
    cmdvel = Twist()

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
        stringdata = data.decode('utf-8')
        stringdata_s = stringdata[1:len(stringdata)-2]
        strings = stringdata_s.split(',')
        strings_n = np.array(strings)
        res = strings_n.astype(np.float)
        print(res)
        a.data = res

        if abs(res[3]) < 0.8:
            cmdvel.angular.z = 0.0
            if abs(abs(res[0])-abs(res[1])) > 0.2:
                cmdvel.angular.z = 0.0
                if abs(res[0]) > abs(res[1]):
                    cmdvel.linear.x = 0.0
                    cmdvel.linear.y = 0.05* res[0]
                else:
                    cmdvel.linear.x = 0.05* res[1]
                    cmdvel.linear.y = 0.0
            else:
                cmdvel.linear.x = 0.0
                cmdvel.linear.y = 0.0
            pub_vel.publish(cmdvel)
        else:
            cmdvel.linear.x = 0.0
            cmdvel.linear.y = 0.0
            cmdvel.angular.z = 0.05* res[3]
            pub_vel.publish(cmdvel)
        pub.publish(a)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass