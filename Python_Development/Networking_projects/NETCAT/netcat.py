#!/usr/bin/env python3
"""
Simple NetCat-like tool for learning.
Features:
 - Connect to a server (client mode)
 - Listen for connections (server mode)
 - Execute a single command on server (--execute)
 - Accept an uploaded file on server (--upload filename)
 - Interactive shell on server (--command)
For safety: test on localhost (127.0.0.1) only unless you have permission.
"""

import argparse
import socket
import threading
import subprocess
import sys

def execute_command(cmd):
    """Run a shell command and return its output (text)."""
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        return output.decode(errors='ignore')
    except subprocess.CalledProcessError as e:
        return e.output.decode(errors='ignore')

class NetCat:
    def __init__(self, args, buffer=b''):
        self.args = args
        self.buffer = buffer
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # allow quick restart
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    # ----- Client side -----
    def send(self):
        self.sock.connect((self.args.target, self.args.port))
        if self.buffer:
            self.sock.sendall(self.buffer)
        try:
            while True:
                data = self.sock.recv(4096)
                if not data:
                    break
                print(data.decode(errors='ignore'), end='')
                # get user input and send
                user_input = input('> ')
                self.sock.sendall((user_input + '\n').encode())
        except KeyboardInterrupt:
            print("\n[+] Client stopping (CTRL-C)")
        finally:
            self.sock.close()

    # ----- Server side -----
    def listen(self):
        self.sock.bind((self.args.target, self.args.port))
        self.sock.listen(5)
        print(f"[+] Listening on {self.args.target}:{self.args.port} ...")
        try:
            while True:
                client_socket, addr = self.sock.accept()
                print(f"[+] Connection from {addr}")
                client_thread = threading.Thread(target=self.handle, args=(client_socket,))
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("\n[+] Server stopping (CTRL-C)")
        finally:
            self.sock.close()

    def handle(self, client_socket):
        # execute one command and return output
        if self.args.execute:
            output = execute_command(self.args.execute)
            client_socket.sendall(output.encode())
            client_socket.close()
            return

        # receive a file and save it
        if self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                file_buffer += data
            try:
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer)
                client_socket.sendall(f"Saved file {self.args.upload}\n".encode())
            except Exception as e:
                client_socket.sendall(f"Failed to save: {e}\n".encode())
            client_socket.close()
            return

        # interactive command shell
        if self.args.command:
            try:
                while True:
                    client_socket.sendall(b'NC-Shell> ')
                    cmd_buffer = b''
                    while b'\n' not in cmd_buffer:
                        chunk = client_socket.recv(64)
                        if not chunk:
                            raise ConnectionResetError()
                        cmd_buffer += chunk
                    cmd = cmd_buffer.decode().strip()
                    if cmd.lower() in ('exit', 'quit'):
                        client_socket.sendall(b'Bye!\n')
                        break
                    if cmd:
                        output = execute_command(cmd)
                        if not output:
                            output = '\n'
                        client_socket.sendall(output.encode())
            except Exception as e:
                print(f"[!] Connection closed or error: {e}")
            finally:
                client_socket.close()
            return

        # default: echo back what client sent
        try:
            while True:
                data = client_socket.recv(4096)
                if not data:
                    break
                client_socket.sendall(b'ECHO: ' + data)
        finally:
            client_socket.close()

def main():
    parser = argparse.ArgumentParser(description="netcat_simple - educational netcat clone")
    parser.add_argument('-l', '--listen', action='store_true', help='listen mode (server)')
    parser.add_argument('-p', '--port', type=int, default=5555, help='port')
    parser.add_argument('-t', '--target', default='127.0.0.1', help='target IP')
    parser.add_argument('-e', '--execute', help='execute a command and return output')
    parser.add_argument('-c', '--command', action='store_true', help='start command shell (server)')
    parser.add_argument('-u', '--upload', help='upon receiving connection, write received bytes to this file')
    args = parser.parse_args()

    if args.listen:
        buffer = b''
    else:
        # read from stdin if anything is piped
        if not sys.stdin.isatty():
            buffer = sys.stdin.buffer.read()
        else:
            buffer = b''

    nc = NetCat(args, buffer)
    nc.run()

if __name__ == '__main__':
    main()
