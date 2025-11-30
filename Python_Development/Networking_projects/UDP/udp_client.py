import socket

target_host = "127.0.0.1"
target_port = 9997
#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
input1 = input("enter the data: ")
input2 = input1.encode()
client.sendto((input2) ,(target_host,target_port))

#receive some data
data,addr = client.recvfrom(4096)
print(data.decode())
client.close()
