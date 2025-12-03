#  Python Networking Projects

A complete collection of practical **Python networking & cybersecurity tools**, including TCP/UDP clients & servers, custom Netcat, proxies, MITM scripts, packet sniffers, and more.

All projects are written for **learning, research, and ethical security testing**.

---

## 📁 Project Structure

<pre>
Networking_projects/
│
├── TCP/             # TCP client, server, port scanner
├── UDP/             # UDP echo server & client
├── NETCAT/          # Custom Python netcat
├── PROXY/           # TCP proxy, intercept tools
├── MITM/            # Man-in-the-middle scripts
├── SNIFFERS/        # Packet sniffers (raw sockets / scapy)
├── TOOLS/           # Utility scripts
└── Resources/       # Word files, sample data
</pre>

---

## ⚡ Quick Setup

<pre>
python3 -m venv env
source env/bin/activate        # on Linux/Mac
env\Scripts\activate           # on Windows
pip install -r requirements.txt
</pre>

Run any tool:

<pre>
python3 TCP/tcp_client.py
python3 UDP/udp_server.py
python3 NETCAT/netcat.py
python3 SNIFFERS/packet_sniffer.py
</pre>

---

## 🔥 Featured Tools

### **1️⃣ TCP Tools**

<pre>
python3 TCP/tcp_client.py
python3 TCP/tcp_server.py
</pre>

✔ TCP basics
✔ Two-way communication
✔ Used for learning connections and sockets

---

### **2️⃣ UDP Tools**

<pre>
python3 UDP/udp_server.py
python3 UDP/udp_client.py
</pre>

✔ Lightweight
✔ Stateless communication
✔ Great for realtime systems

---

### **3️⃣ Custom Netcat (Python Version)**

<pre>
python3 NETCAT/netcat.py -t &lt;ip&gt; -p &lt;port&gt; -l
</pre>

Supports:
✔ Listening mode
✔ Reverse shell
✔ File transfer
✔ Data piping

---

### **4️⃣ TCP Proxy**

<pre>
python3 PROXY/tcp_proxy.py &lt;local_port&gt; &lt;remote_host&gt; &lt;remote_port&gt;
</pre>

✔ Intercept traffic
✔ Forward packets
✔ Modify requests/responses
✔ MITM-style analysis

---

### **5️⃣ MITM Tools**

Scripts include:

* HTTP MITM
* Traffic relay
* Logging requests/responses

<pre>
python3 MITM/mitm_http.py
</pre>

---

### **6️⃣ Packet Sniffers**

<pre>
sudo python3 SNIFFERS/packet_sniffer.py
</pre>

✔ Captures live traffic
✔ Shows protocols, hosts, ports
✔ Ideal for network analysis

---

## 🧪 Example Output

<pre>
[+] Connection from 192.168.1.10:55312
[>] Received: GET /index.html HTTP/1.1
</pre>

---

## 🎯 Purpose of This Repository

This repo is designed to help you master:

* Socket programming
* TCP / UDP internals
* Network protocols
* Low-level packet handling
* Writing real hacker-style tools
* Building cybersecurity confidence

Everything is clean, minimal, and beginner-friendly.

---

## 🛡 Ethical Use Warning

This project is meant for **learning and legal penetration testing only**.
Never run these tools on systems without permission.

---
