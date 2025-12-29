# FTP Brute Force

A Python script for brute-forcing FTP login credentials using a customizable wordlist. Designed for educational purposes to demonstrate security concepts.

## Features

- **Multithreading**: Parallel password attempts for improved performance.
- **Colorful Output**: Enhanced readability with colorama library.
- **Simple Interface**: Command-line prompts for easy configuration.

## Installation

1. Clone the repository
2. Install dependencies:  
   `pip install colorama`

## Usage

Run the script and follow the prompts  

- Enter the FTP server hostname or IP address.
- Provide the username.
- Specify the port (default is 21).

The script will attempt logins using passwords from `wordlist.txt`.

## Configuration

- **Threads**: Modify `n_thread` in the script (default: 30) to adjust parallel execution.
- **Wordlist**: Update `wordlist.txt` with your password list, one per line.

## Disclaimer

This script is intended for educational purposes only. Unauthorized access to systems is illegal and unethical. Use only on systems you own or have explicit permission to test. The author is not responsible for misuse.
