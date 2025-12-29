# Ransomware Educational Project

A Python-based simulation of ransomware for educational purposes, demonstrating encryption techniques and security concepts in a controlled environment.

## Features

- **File Encryption**: Uses Fernet and RSA to encrypt files in a target directory.
- **Ransom Note**: Generates notes and alters desktop background.
- **Key Management**: Includes tools for RSA key generation and Fernet key decryption.

## Components

- **ransomware.py**: Encrypts files and displays ransom demands.
- **Decrypt_fernet_key.py**: Decrypts the Fernet key using RSA private key.
- **RSA_key_generator.py**: Generates RSA key pairs.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt` (`pip install -r requirements.txt`)

## Installation

Clone the repository and install dependencies.

## Usage

1. Generate RSA keys using the key generator script.
2. Run the ransomware script on a test directory to simulate encryption.
3. Use the decryption script to recover the Fernet key and decrypt files.

## Disclaimer

This project is purely educational. Unauthorized use for malicious purposes is illegal and unethical. The authors are not responsible for any damage caused by misuse. Use responsibly and legally.
