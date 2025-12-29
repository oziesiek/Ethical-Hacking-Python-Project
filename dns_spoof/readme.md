# DNS Spoofing

A Python script using netfilterqueue and Scapy to perform DNS spoofing attacks, redirecting DNS queries for a specific domain to a spoofed IP address.

## Features

- **Packet Interception**: Captures DNS packets via netfilterqueue.
- **Domain Spoofing**: Modifies responses for targeted domains (e.g., www.bing.com).
- **IP Redirection**: Routes traffic to a custom IP address.

## Requirements

- Python 3.x
- netfilterqueue library (`pip install netfilterqueue`)
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Set up iptables to forward DNS packets to NFQUEUE (e.g., `iptables -I FORWARD -j NFQUEUE --queue-num 0`). Run the script to spoof DNS responses.

## Disclaimer

This script is for educational purposes only. DNS spoofing is illegal without permission. Use only on authorized networks. The creator is not responsible for misuse. Comply with laws.
