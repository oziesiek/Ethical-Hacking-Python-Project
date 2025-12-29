# HTTP Content Injection

A Python script using netfilterqueue and Scapy to intercept and modify HTTP traffic, injecting custom JavaScript into responses for educational demonstrations of man-in-the-middle attacks.

## Features

- **Traffic Interception**: Uses netfilterqueue to capture packets.
- **Request Modification**: Removes Accept-Encoding headers.
- **Response Injection**: Adds JavaScript hooks before </body> and updates Content-Length.

## Requirements

- Python 3.x
- netfilterqueue library (`pip install netfilterqueue`)
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Set up iptables to forward packets to NFQUEUE (e.g., `iptables -I FORWARD -j NFQUEUE --queue-num 0`). Run the script to perform content injection on HTTP traffic.

## Disclaimer

This script is for educational purposes only. HTTP injection is illegal without permission. Use only on authorized networks. The creator is not responsible for misuse. Comply with laws.
