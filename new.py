import socket
import struct

import pyMultiWii

# Define the IP address and port of the serial-to-TCP/IP adapter
TCP_IP = '192.168.4.2'
TCP_PORT = 23

# Connect to the serial-to-TCP/IP adapter
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Create a MultiWii object for communication with the flight controller
board = pyMultiWii.MultiWii("/dev/null")

# Define the desired pitch, roll, yaw, and throttle values
pitch = 0
roll = 0
yaw = 0
throttle = 1200

# Encode the desired values as a binary message
message = struct.pack('<4h', pitch, roll, yaw, throttle)

# Send the message to the flight controller over the serial-to-TCP/IP connection
s.sendall(message)

# Close the connection to the serial-to-TCP/IP adapter
s.close()