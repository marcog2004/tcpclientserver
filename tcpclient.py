# Marco Greco 40285114
# COEN 366 Lab 2 TCP Client
# Adapted from Lab slides

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)
print("Connected to Server.")

initial_time = time.time() # store initial time to wait specified time (5 minutes in lab manual)

TOTAL_TIME = 300 # total time of message sending
DELAY = 60 # delay between messages

try:
    while time.time() - initial_time < TOTAL_TIME: # keep sending messages until total time is reached
        # Send data
        message = 'test' # message to send
        sock.sendall(message.encode('utf-8')) # encode into byte format and send to server
        start = time.time() # record time when message is sent

        # Look for the response
        data = sock.recv(16) # receive data back from server
        end = time.time() # record time after receiving data

        print(f"Received: PONG {len(data)} {data.decode()} | RTT = {(end - start)*1000:.3f} ms") # display PONG message with size of data, data and round trip time
        time.sleep(DELAY)

finally: # close socket
    sock.close()
    sys.exit()