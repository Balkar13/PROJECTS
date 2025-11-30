import socket

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9999))  # IP + PORT
server.listen(5)  # Allow max 5 pending connections

print("TCP Server running on 127.0.0.1:9999 ...")

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr}")

    # Receive data from client
    data = client_socket.recv(1024)
    print("Client sent:", data.decode())

    # Send response
    client_socket.send(b"Message received by TCP server")

    client_socket.close()
