import sys
import time
import platform
import socket

#from multiprocessing import shared_memory
ip = "127.0.0.1"
port = 9999

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((ip,port))

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

a = [0.0,0.0,0.0,0.0]
b = str(a)
c = bytes(b, 'utf-8')
socket_client.send(c)
time.sleep(0.1)

#Check that the 3dRudder 1 is connected
while not sdk.IsDeviceConnected (nPortNumber):
    print("3dRudder is not Connected")
    time.sleep(1)
    
#Get Version of The Firmware
version=sdk.GetVersion(nPortNumber)
print ("Version FirmWare : {:1x}".format(version))

#Get the number of the 3dRudder are connected
print ("Get the Number of the 3dRudder are connected : {:1x}".format(sdk.GetNumberOfConnectedDevice()))

#Play a sound wih the 3dRuddermjnhbh                                       
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


print("Initialize Finished")

rollDeadzone = 5
rollXSat = 18
rollYMax = 1
rollExp = 4
pitchDeadzone = 5
pitchXSat = 18
pitchYMax = 1
pitchExp = 4
yawDeadzone = 5
yawXSat = 18
yawYMax = 1
yawExp = 4
curves=CurveArray()

print("Roll")
roll=Curve()
#rollDeadzone = float(input("Set roll deadzone(deg), Max is 18 deg : "))
roll.SetDeadZone(rollDeadzone/18)
#rollXSat = float(input("Set roll XSat(deg), Max is 18 deg : "))
roll.SetXSat(rollXSat/18)
#rollYMax = float(input("Set roll YMax : "))
roll.SetYMax(rollYMax)
#rollExp = float(input("Set roll Exp : "))
roll.SetExp(rollExp)
curves.SetCurve(CurveRoll,roll)
print(" ")

print("Pitch")
pitch=Curve()
#pitchDeadzone = float(input("Set pitch deadzone(deg), Max is 18 deg : "))
pitch.SetDeadZone(pitchDeadzone/18)
#pitchXSat = float(input("Set pitch XSat(deg), Max is 18 deg : "))
pitch.SetXSat(pitchXSat/18)
#pitchYMax = float(input("Set pitch YMax : "))
pitch.SetYMax(pitchYMax)
#pitchExp = float(input("Set pitch Exp : "))
pitch.SetExp(pitchExp)
curves.SetCurve(CurvePitch,pitch)
print(" ")

print("Yaw")
yaw=Curve()
print()
#yawDeadzone = float(input("Set yaw deadzone(deg), Max is 25 deg : "))
yaw.SetDeadZone(yawDeadzone/25)
#yawXSat = float(input("Set yaw XSat(deg), Max is 25 deg : "))
yaw.SetXSat(yawXSat/25)
#yawYMax = float(input("Set yaw YMax : "))
yaw.SetYMax(yawYMax)
#yawExp = float(input("Set yaw Exp : "))
yaw.SetExp(yawExp)
curves.SetCurve(CurveYaw,yaw)
print(" ")

axis = Axis()
while(sdk.GetStatus(nPortNumber)<8):
    print ("Sensor  Value : [{:d},{:d},{:d},{:d},{:d},{:d}] ".format(sdk.GetSensor( nPortNumber ,0 ),sdk.GetSensor( nPortNumber , 1 ),sdk.GetSensor( nPortNumber , 2 ),sdk.GetSensor( nPortNumber , 3 ),sdk.GetSensor( nPortNumber , 4 ),sdk.GetSensor( nPortNumber , 5 )))
    axis = Axis()
    sdk.GetAxis(0,NormalizedValue,axis)
    print ("Axis NormalizedValue Value : [{:.2f},{:.2f},{:.2f},{:.2f}]".format(axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ)) 
    a = [axis.m_aX,axis.m_aY,axis.m_aZ,axis.m_rZ]
    b = str(a)
    c = bytes(b, 'utf-8')
    socket_client.send(c)
    time.sleep(0.1)