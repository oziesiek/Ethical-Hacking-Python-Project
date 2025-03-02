![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

# Rootkit

Rootkit is a Python script designed to demonstrate the concept of process disguise and persistence on Linux systems. This project aims to provide educational insights into how rootkits can operate by changing process names and establishing persistence through system services.

## Features

- **Process Disguise**: Changes the process name to mimic common system processes, enhancing stealth.
- **Persistence**: Automatically installs a systemd service to ensure the script runs at startup.
- **Educational Purpose**: Serves as a learning tool for understanding rootkit behavior and system security.

## Installation

### Prerequisites

- Python 3.x
- `setproctitle` library

## Usage

To run the application, execute the following command:
python3 rootkit.py


## Disclaimer

This project is intended for educational purposes only.
