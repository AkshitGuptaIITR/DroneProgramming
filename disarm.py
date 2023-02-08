import pyMultiWii
import time

myDrone = pyMultiWii.pyMultiWii('192.168.4.1', 23)

# myDrone.setThrottle(1000)
# myDrone.arm()

myDrone.disarm()
