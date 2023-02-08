import pyMultiWii
import time

myDrone = pyMultiWii.pyMultiWii('192.168.4.1', 23)

myDrone.arm() 
startTime = time.time()
endTime=time.time();
elapsedTime=0;

# startrepeat("print('Hello World')", .01)

print(myDrone.recieveResponse(), "Response Recived \n")
for x in range (1000,1801,10):
  myDrone.setThrottle(x) 
  time.sleep(0.1)
  
  
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Elapsed Time = %s" % elapsedTime)

print("1800 reached");

startTime = time.time()
endTime = time.time()
elapsedTime = endTime - startTime
while(elapsedTime<=1):
  myDrone.setThrottle(1800)
  endTime = time.time()
  elapsedTime = endTime - startTime

print("height reached")

for x in range (1800,1499,-10):
  myDrone.setThrottle(x) 
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Elapsed Time = %s" % elapsedTime)

print("1500 reached")

startTime = time.time()
endTime = time.time()
elapsedTime = endTime - startTime

# while(elapsedTime<=8):
#   myDrone.setThrottle(1500)
#   endTime = time.time()
#   elapsedTime = endTime - startTime
print("start pitch")
for x in range (1500,1602,2):
  myDrone.setThrottle(1500)
  myDrone.setPitch(x) 
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime

print("constant pitch")
while(elapsedTime<=2):
  myDrone.setThrottle(1500)
  myDrone.setPitch(1600)
  endTime = time.time()
  elapsedTime = endTime - startTime

print("ending pitch")
for x in range (1600, 1499, -2): 
  myDrone.setThrottle(1500)
  myDrone.setPitch(x)
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("const pitch")
startTime = time.time()
endTime = time.time()
elapsedTime = endTime - startTime
while(elapsedTime<=4):
  myDrone.setThrottle(1500)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("constant")
print("start reverse pitch")
for x in range (1500,1400,-2):
  myDrone.setThrottle(1500)
  myDrone.setPitch(x) 
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime

print("constant reverse pitch")
while(elapsedTime<=2):
  myDrone.setThrottle(1500)
  myDrone.setPitch(1400)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("const rev pitch")

print("ending reverse pitch")
for x in range (1400, 1501, 2): 
  myDrone.setThrottle(1500)
  myDrone.setPitch(x)
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime
# for x in range (1500,1550,2):
#   myDrone.setThrottle(1500)
#   myDrone.setRoll(x) 
#   time.sleep(0.1)
#   endTime = time.time()
#   elapsedTime = endTime - startTime
# for x in range (1500,1450,-2):
#   myDrone.setThrottle(1500)
#   myDrone.setPitch(x) 
#   time.sleep(0.1)
#   endTime = time.time()
#   elapsedTime = endTime - startTime
# for x in range (1500,1490,-2):
#   myDrone.setThrottle(1500)
#   myDrone.setRoll(x) 
#   time.sleep(0.1)
#   endTime = time.time()
#   elapsedTime = endTime - startTime
  

print("reducing throtle")

for x in range (1500,999,-5):
  myDrone.setThrottle(x) 
  time.sleep(0.1)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Elapsed Time = %s" % elapsedTime)
  

print("fuck of");  
myDrone.disarm() 
# for t in range (0,1000):

# time.sleep(2)  

# myDrone.setPitch(1000)
  
# data = myDrone.getData(pyMultiWii.ATTITUDE)

# altitude = data["altitude"]
# print("Altitude : ",altitude)