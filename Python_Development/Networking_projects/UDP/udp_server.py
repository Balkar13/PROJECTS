import socket

#declare host and port in variable
target_host = "127.0.0.1"
target_port = 9997

#create socket object
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(("127.0.0.1",9997))
print("UDP server is running on 127.0.0.1:9997 ...")

while True:
#receive
    data,addr = server.recvfrom(4096)

    print(f"data received from: {addr}: {data.decode()}")
    server.sendto(b"received data successfully",addr)

