# Deauther Attack

A Python script using Scapy to perform wireless deauthentication attacks by sending de-authentication frames to disconnect devices from a network. Intended for educational purposes in ethical hacking and network security testing.

## Features

- **Targeted Deauth**: Sends packets to specific devices via router MAC.
- **Configurable**: Adjustable packet count and network interface.
- **Verbose Output**: Detailed sending information.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)

## Installation

Clone the repository and install dependencies.

## Usage

Edit the script to set `target_mac` and `gateway_mac` with the appropriate MAC addresses. Run the script.

To obtain the router MAC address: Use `iw dev [interface] link` after identifying your Wi-Fi interface with `ifconfig`.

## Configuration

- **Interface**: Update `iface` (e.g., "wlan0") for your network adapter.
- **Packet Count**: Modify `count` (default: 100) for the number of deauth frames.

## Disclaimer

This script is for educational purposes only. Unauthorized deauthentication attacks are illegal. Use only on networks you own or have permission to test. The author is not responsible for misuse.
