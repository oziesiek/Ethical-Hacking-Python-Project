# Reverse Backdoor - Listener and Backdoor

A Python-based Remote Access Tool for educational purposes, demonstrating networking and command execution concepts through a listener and backdoor pair.

## Features

- **Listener**: Runs on attacker machine, accepts connections, provides CLI for remote interaction.
- **Backdoor**: Runs on target, connects back, executes commands, handles file transfers.
- **Commands**: Execute system commands, change directories, upload/download files.

## Requirements

- Python 3.x
- Socket library (built-in)

## Installation

Clone the repository and install dependencies.

## Usage

Configure IP and port in both scripts. Run the listener first, then the backdoor on the target. Use the listener's CLI to send commands.

## Disclaimer

This tool is for educational purposes only. Unauthorized access is illegal and unethical. Use only on authorized systems. The authors are not responsible for misuse. Stay ethical.
