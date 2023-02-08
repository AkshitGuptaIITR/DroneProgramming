import pyMultiWii
import time

myDrone = pyMultiWii.pyMultiWii('192.168.4.1', 23)

myDrone.arm()
# time.sleep(2)
# while(True):
myDrone.setThrottle(1000)

time.sleep(2)
myDrone.setThrottle(1200)
time.sleep(2)
myDrone.setThrottle(1500)
# time.sleep(2)
# myDrone.setThrottle(1000)
# time.sleep(2)
# myDrone.disarm()
