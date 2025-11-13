import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)
print("Connected to Server.")

try:

    for i in range(5):
        # Send data
        message = 'test'
        sock.sendall(message.encode('utf-8'))
        start = time.time()

        # Look for the response
        data = sock.recv(16)
        end = time.time()

        print(f"Received: PONG {len(data)} {data.decode()} | RTT = {(end - start)*1000:.3f} ms")

finally:
    sock.close()
    sys.exit()