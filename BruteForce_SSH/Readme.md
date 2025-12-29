# SSH Brute Force

A Python script for brute-forcing SSH login credentials using the Paramiko library. Designed for educational purposes to demonstrate security concepts.

## Features

- **Custom Lists**: Supports username and password lists.
- **Colored Output**: Enhanced visibility with colorama.
- **Retry Mechanism**: Automatic delay on quota exceeded.
- **Credential Saving**: Saves successful logins to a file.

## Requirements

- Python 3.x
- Paramiko library (`pip install paramiko`)
- Colorama library (`pip install colorama`)

## Installation

Clone the repository and install dependencies.

## Usage

Run the script with the target host, username, and password list file:  

`python ssh_bruteforce.py <host> -u <username> -P <password_list_file>`  

Example:  
`python ssh_bruteforce.py 192.168.1.1 -u admin -P passwords.txt`

## Disclaimer

This script is intended for educational purposes only. Unauthorized access to systems is illegal and unethical. Use only on systems you own or have explicit permission to test. The author is not responsible for misuse.
