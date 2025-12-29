# File Replacement Attack

A Python script using netfilterqueue and Scapy to perform file replacement attacks on HTTP traffic, redirecting .exe file downloads to a malicious URL.

## Features

- **Traffic Interception**: Captures HTTP requests via netfilterqueue.
- **File Detection**: Identifies downloads of .exe files.
- **Redirection**: Sends 301 responses to spoofed URLs.

## Requirements

- Python 3.x
- netfilterqueue library (`pip install netfilterqueue`)
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Set up iptables to forward packets to NFQUEUE (e.g., `iptables -I FORWARD -j NFQUEUE --queue-num 0`). Run the script to intercept and redirect .exe downloads.

## Disclaimer

This script is for educational purposes only. File replacement attacks are illegal without permission. Use only on authorized networks. The creator is not responsible for misuse. Comply with laws.
