# Marco Greco 40285114
# COEN 366 Lab 2 TCP Server
# Adapted from Lab slides

import socket
import sys

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IPv4 // SOCK_STREAM -> TCP
server_address = ('localhost', 10000) # Store IP Address + Port

sock.bind(server_address) # Assign Address and Port to socket

# Server starts listening on the port
sock.listen(1)

while True:
    # Wait for a connection
    print("TCP Server waiting for client.", file=sys.stderr)
    connection, client_address = sock.accept() # Accept connection from client
    try:
        print("Client Connected:  %s" % (client_address,), file=sys.stderr)
        # Wait for data
        while True:
            data = connection.recv(16) # Receive data
            if data:
                print(f"Received: PING {len(data)} {data.decode('utf-8')}", file=sys.stderr) # Display PING message with size of data and data
                connection.sendall(data) # send data back
            else:
                break

    finally:
        # Clean up the connection
        connection.close()
        sock.close()
        sys.exit()