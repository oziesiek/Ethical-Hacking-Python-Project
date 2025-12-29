# PDF Password Cracker

A Python script for decrypting password-protected PDF files using a wordlist. Leverages `pikepdf` for PDF handling and provides colorful output for user feedback.

## Features

- **Interactive Prompts**: Requests PDF file and wordlist paths.
- **Progress Tracking**: Uses tqdm for decryption progress.
- **Colorful Interface**: Banner and success messages with colorama.
- **Efficient Cracking**: Iterates through passwords until success.

## Requirements

- Python 3.x
- pikepdf library (`pip install pikepdf`)
- tqdm library (`pip install tqdm`)
- colorama library (`pip install colorama`)

## Installation

Clone the repository and install dependencies.

## Usage

Run the script and follow the prompts to provide the PDF file and wordlist. The script will attempt decryption and display the found password.

## Disclaimer

This script is for educational purposes only. Use only on PDFs you own or have permission to access. Cracking unauthorized files is illegal. The author is not responsible for misuse.
