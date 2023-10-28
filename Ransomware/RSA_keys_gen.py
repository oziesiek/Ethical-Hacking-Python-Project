from Crypto.PublicKey import RSA  # Import RSA key generation functionality
from Crypto.Cipher import PKCS1_OAEP  # Import PKCS1_OAEP cipher algorithm from Crypto library
from Crypto.Random import get_random_bytes  # Import function to generate random bytes

# Check Python version and handle input compatibility for both Python 2 and 3
try:
    input = raw_input  # For Python 2 compatibility, reassign input to raw_input
except NameError:
    pass  # For Python 3, raw_input is already input

# Function to generate RSA encryption-decryption keys (public-private keys)
def generate_keys():
    key = RSA.generate(2048)  # Generate an RSA key pair of 2048 bits

    # Export private key and save it to 'private.pem' file
    private_key = key.exportKey()
    with open('private.pem', 'wb') as f:
        f.write(private_key)

    # Export public key and save it to 'public.pem' file
    public_key = key.publickey().exportKey()
    with open('public.pem', 'wb') as f:
        f.write(public_key)

    print("RSA keys generated and saved.")  # Print a message indicating key generation completion

# Function to encrypt a Fernet key using the RSA public key
def encrypt_fernet_key():
    print('> Encryption')  # Print a message indicating encryption process

    public_key = RSA.importKey(open('public.pem').read())  # Import the RSA public key from 'public.pem' file

    # Generate a random Fernet key (32 bytes) and save it to 'fernet_key.txt'
    fernet_key = get_random_bytes(32)
    with open('fernet_key.txt', 'wb') as f:
        f.write(fernet_key)

    public_crypter = PKCS1_OAEP.new(public_key)  # Create a public key encrypter using PKCS1_OAEP padding scheme

    # Encrypt the Fernet key and save the encrypted key to 'enc_fernet_key.txt'
    with open('fernet_key.txt', 'rb') as f:
        fernet_key = f.read()
        enc_fernet_key = public_crypter.encrypt(fernet_key)
        with open('enc_fernet_key.txt', 'wb') as f:
            f.write(enc_fernet_key)

    print('> Fernet key encrypted and saved.')  # Print a message indicating encryption completion

# Function to decrypt an encrypted Fernet key using the RSA private key
def decrypt_fernet_key():
    print("> Decryption")  # Print a message indicating decryption process

    private_key = RSA.importKey(open('private.pem').read())  # Import the RSA private key from 'private.pem' file

    # Read the encrypted Fernet key from 'enc_fernet_key.txt' file
    with open('enc_fernet_key.txt', 'rb') as f:
        enc_fernet_key = f.read()

    private_crypter = PKCS1_OAEP.new(private_key)  # Create a private key decrypter using PKCS1_OAEP padding scheme

    # Decrypt the encrypted Fernet key and save the decrypted key to 'dec_fernet_key.txt'
    dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
    with open('dec_fernet_key.txt', 'wb') as f:
        f.write(dec_fernet_key)

    print('> Fernet key decrypted and saved.')  # Print a message indicating decryption completion

# Main program loop
while True:
    # Prompt user to choose an option: key generation, encryption, or decryption
    option = input("Choose an option: 1 (Generate RSA Keys), 2 (Encrypt Fernet Key), 3 (Decrypt Fernet Key): ").strip()

    # Perform the corresponding action based on user input
    if option == "1":
        generate_keys()  # Call generate_keys() function to generate RSA keys
        break  # Exit the loop after generating keys
    elif option == "2":
        encrypt_fernet_key()  # Call encrypt_fernet_key() function to encrypt Fernet key
        break  # Exit the loop after encryption
    elif option == "3":
        decrypt_fernet_key()  # Call decrypt_fernet_key() function to decrypt Fernet key
        break  # Exit the loop after decryption
    else:
        print("Invalid option. Please choose 1, 2, or 3.")  # Print an error message for invalid input
