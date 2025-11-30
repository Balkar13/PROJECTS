import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9999))

# Send data
client.send(b"Hello Server, this is Balkar!")

# Receive server reply
response = client.recv(4096)

print("Server:", response.decode())

client.close()

