# Shodan DVWA Credential Checker

A Python script that leverages the Shodan API to locate Damn Vulnerable Web Application (DVWA) instances and tests default credentials (admin:password) by handling CSRF tokens.

## Features

- **Shodan Integration**: Searches for DVWA hosts using Shodan.
- **Credential Testing**: Automates login attempts with default creds.
- **CSRF Handling**: Retrieves and uses CSRF tokens for authentication.

## Requirements

- Python 3.x
- Shodan API key (obtain from [Shodan](https://account.shodan.io/))

## Installation

Clone the repository and install dependencies.

## Usage

Run the script with your Shodan API key configured. It will search for DVWA instances and attempt logins with default credentials.

## Disclaimer

This script is for educational purposes only. Testing credentials on unauthorized systems is illegal. Use only on your own instances or with permission. The author is not responsible for misuse.
