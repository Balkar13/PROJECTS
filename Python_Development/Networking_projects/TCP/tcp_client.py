import socket
ip = "127.0.0.1"
port = 9999
# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))

# Send data
input1 = input(f"Enter Message for {ip} {port} : ").encode()
client.send(input1)

# Receive server reply
response = client.recv(4096)

print("Server:", response.decode())

client.close()

