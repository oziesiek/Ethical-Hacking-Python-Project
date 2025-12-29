# HTTP Packet Sniffer

A Python script using Scapy to capture and analyze HTTP packets on a network interface, extracting URLs and potential login credentials for educational security analysis.

## Features

- **Packet Capture**: Sniffs HTTP traffic on specified interfaces.
- **Credential Detection**: Identifies and logs possible usernames, passwords, or emails.
- **URL Extraction**: Displays requested URLs from captured requests.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Run the script to start sniffing on the default interface (eth0) or modify for another. It will display captured HTTP data.

## Disclaimer

This script is for educational purposes only. Packet sniffing without permission is illegal. Use only on authorized networks. The creator is not responsible for misuse. Comply with laws.
