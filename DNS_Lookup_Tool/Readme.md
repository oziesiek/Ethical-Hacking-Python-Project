# DNS Lookup Tool

A Python script for performing DNS lookups on a target domain with specified record types using the `dns.resolver` module. Ideal for network diagnostics and educational exploration.

## Features

- **Flexible Record Types**: Query multiple DNS record types or use defaults.
- **Interactive Prompts**: User-friendly input for domain and records.
- **Error Handling**: Gracefully skips unresolvable records.

## Requirements

- Python 3.x
- dnspython library (`pip install dnspython`)

## Installation

Clone the repository and install dependencies.

## Usage

Run the script and follow the prompts

Enter the target domain and record types (space-separated, or press Enter for defaults: A, AAAA, CNAME, MX, NS, SOA, TXT). View the resolved records.

## Disclaimer

This script is intended for educational purposes only. Use responsibly and only on domains you have permission to query. The author is not responsible for misuse.
