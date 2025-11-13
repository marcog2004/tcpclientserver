import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)

print("starting up on %s port %s" % server_address, file=sys.stderr)
sock.bind(server_address)

# Server starts listening on the port
sock.listen(1)

while True:
    # Wait for a connection
    print("TCP Server waiting for client.", file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print("Client Connected:  %s" % (client_address,), file=sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            if data:
                print(f"Received: PING {len(data)} {data.decode('utf-8')}", file=sys.stderr)
                connection.sendall(data)
            else:
                break

    finally:
        # Clean up the connection
        connection.close()
        sock.close()
        sys.exit()