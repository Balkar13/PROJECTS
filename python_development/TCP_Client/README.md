# 🛰️ TCP Client (Python)

This file is a simple TCP Client built using Python’s `socket` module.

It connects to a TCP Server, sends messages, and receives responses.

---

## ⚙️ How It Works

1. The client creates a socket using:
   ```python
   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
It connects to the server’s IP and port.

Sends data using:client.send(data.encode())
Receives the server’s response using:client.recv(1024)

*** How to Run ***

Make sure you have Python 3 installed.

Clone or download the project.

Run the server first (if you have one): python tcp_server.py
Run the client:python tcp_client.py

Enter your message when prompted.

Example Output
Connected to server at 127.0.0.1:4444
Enter message: Hello Server!
Server Response: Hello Client!

Requirements

Python 3.x

Basic understanding of sockets and networking

You can modify the IP and PORT inside the script:

server_ip = "127.0.0.1"
server_port = 4444


This project is for educational purposes only.
Feel free to modify or improve it.
