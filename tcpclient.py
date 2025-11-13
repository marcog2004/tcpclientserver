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

initial_time = time.time()

TOTAL_TIME = 300
DELAY = 60

try:
    while time.time() - initial_time < TOTAL_TIME:
        # Send data
        message = 'test'
        sock.sendall(message.encode('utf-8'))
        start = time.time()

        # Look for the response
        data = sock.recv(16)
        end = time.time()

        print(f"Received: PONG {len(data)} {data.decode()} | RTT = {(end - start)*1000:.3f} ms")
        time.sleep(DELAY)

finally:
    sock.close()
    sys.exit()