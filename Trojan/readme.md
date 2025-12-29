# Educational Malicious Downloader

A Python script simulating a malicious downloader for educational purposes, demonstrating file download, execution, and cleanup in a controlled environment.

## Features

- **File Downloads**: Retrieves a PDF and executable from a specified URL.
- **Execution**: Opens the PDF with the default viewer and runs the executable.
- **Cleanup**: Removes downloaded files from the temp directory.

## Requirements

- Python 3.x
- Internet connection for downloads

## Installation

Clone the repository and install dependencies.

## Usage

Run the script to simulate the download and execution process. Replace placeholder URLs with test addresses for safe analysis.

## Compilation

Use PyInstaller to compile into an executable:

- **Windows/Linux**: `pyinstaller --onefile --noconsole --icon=icon.ico script_name.py`
- **macOS**: `pyinstaller --onefile --noconsole --icon=icon.icns script_name.py`

The executable will be in the `dist` directory.

## Disclaimer

This script is for educational and informational purposes only. Unauthorized use for malicious purposes is strictly prohibited. Handle unfamiliar code with caution. The author is not responsible for misuse.
