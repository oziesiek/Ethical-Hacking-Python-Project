# ARP Spoofing

A Python script using Scapy to perform ARP spoofing attacks on a local network, tricking a target device and the gateway into routing traffic through the attacker's machine.

## Features

- **MAC Retrieval**: Obtains MAC addresses via ARP requests.
- **Spoofing Function**: Sends forged ARP packets to poison caches.
- **Restoration**: Resets ARP tables to original state.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Run the script with appropriate permissions on your network. It will perform ARP spoofing between a target and the gateway.

## Disclaimer

This script is for educational purposes only. ARP spoofing is illegal without authorization. Use only on networks you own or have permission to test. The creator is not responsible for misuse. Comply with laws.
