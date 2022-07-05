#!/usr/bin/env python

import sys
import time
import platform
import rospy
from std_msgs.msg import Float32MultiArray

def talker():
    
    print("a")
    rospy.init_node('mobileInterface', anonymous=True)
    pub = rospy.Publisher('mobileCommand', Float32MultiArray, queue_size=1)

    aa = 2
    a = Float32MultiArray()
    a.data = [5.0, 3.0]
    while aa > 1:
        pub.publish(a)
        time.sleep(2)

    '''
    # 32 or 64 bit
    val_max=platform.architecture()

    print(val_max[0])
    if (val_max[0]=='32bit') : 
        from win32.Python363.ns3DRudder import * #import SDk 3dRudder
    else:
        from x64.Python363.ns3DRudder import * #import SDk 3dRudder

    #define the Status of the 3dRudder
    status_3dRudder = [ "None",
                        "Puts the 3DRudder on the floor",
                        "The 3dRudder initialize for about 2 seconds",
                        "Put your first feet on the 3dRudder",
                        "Put your second Foot on the 3dRudder",
                        "The user must wait still for half a second for calibration until a last short beep is heard from the device. The 3DRudder is ready to be used.",
                        "The 3dRudder is in use",
                        "The 3dRudder is in use and is fully operational with all the features enabled"
                        ]


    #Init SDk 3dRudder
    sdk=GetSDK()
    sdk.Init()

    # 3dRudder 1
    nPortNumber=0
        
    #Check that the 3dRudder 1 is connected
    while not sdk.IsDeviceConnected (nPortNumber):
        print("3dRudder is not Connected")
        time.sleep(1)
        
    #Get Version of The Firmware
    version=sdk.GetVersion(nPortNumber)
    print ("Version FirmWare : {:1x}".format(version))

    #Get the number of the 3dRudder are connected
    print ("Get the Number of the 3dRudder are connected : {:1x}".format(sdk.GetNumberOfConnectedDevice()))

    #Play a sound wih the 3dRudder
    sdk.PlaySnd(nPortNumber,1000,2000)
    print(sdk.GetStatus(nPortNumber))
    while(sdk.GetStatus(nPortNumber)<6):
        i = sdk.GetStatus(nPortNumber)
        if(i<3):
            print("3drudder init...")
        elif(i==3):
            print("Put your first feet on the 3drudder")
        elif(i==4):
            print("Put your second feet on the 3drudder")
        elif(i==5):
            print("wait...")

        time.sleep(1)

    print("Initialize Finished")

    axis = Axis()
    while(sdk.GetStatus(nPortNumber)<8):
        print ("Sensor  Value : [{:d},{:d},{:d},{:d},{:d},{:d}] ".format(sdk.GetSensor( nPortNumber ,0 ),sdk.GetSensor( nPortNumber , 1 ),sdk.GetSensor( nPortNumber , 2 ),sdk.GetSensor( nPortNumber , 3 ),sdk.GetSensor( nPortNumber , 4 ),sdk.GetSensor( nPortNumber , 5 )))
        axis = Axis()
        sdk.GetAxis(0,NormalizedValue,axis)
        print ("Axis NormalizedValue Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 
        time.sleep(0.1)
     '''

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterryptException:
        pass