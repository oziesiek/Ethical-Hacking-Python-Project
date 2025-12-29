# Fake WiFi Beacon

A Python script using Scapy to send wireless beacon frames, simulating multiple fake access points for educational purposes in ethical hacking and network security testing.

## Features

- **Multiple Simulations**: Generates random SSIDs and MAC addresses for multiple APs.
- **Threaded Sending**: Concurrent beacon transmission for realism.
- **Configurable**: Adjustable number of APs and network interface.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)
- Faker library (`pip install faker`)

## Installation

Clone the repository and install dependencies.

## Usage

Edit the script to set `sender_mac` with your desired MAC address. Run the script.

The script will simulate and broadcast beacon frames for the configured number of access points.

## Configuration

- **Number of APs**: Update `n_ap` (default: 5) for the count of simulated access points.
- **Interface**: Set `iface` (e.g., "wlan0") to your wireless network adapter.
- **Sender MAC**: Replace `sender_mac` with your chosen MAC address.

## Disclaimer

This script is for educational purposes only. Simulating fake access points can disrupt networks and is illegal without permission. Use only on your own networks. The author is not responsible for misuse.
