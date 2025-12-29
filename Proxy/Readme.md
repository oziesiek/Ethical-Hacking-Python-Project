# HTTP Overlay Injector

A mitmproxy script for injecting image overlays and JavaScript alerts into HTML responses during man-in-the-middle attacks. Useful for educational demonstrations of web security vulnerabilities.

## Features

- **Header Removal**: Strips security headers like CSP and HSTS.
- **Overlay Injection**: Adds a semi-transparent image overlay to HTML pages.
- **Alert Display**: Triggers a JavaScript alert blocking interactions.

## Requirements

- Python 3.x
- mitmproxy library (`pip install mitmproxy`)

## Installation

Clone the repository and install dependencies.

## Usage

Run mitmproxy with the script and configure your browser to use the proxy (default: 127.0.0.1:8080). Visit target websites to see the injected overlays.

## Configuration

- **Overlay Content**: Modify `OVERLAY_HTML` and `OVERLAY_JS` for custom image URLs and alerts.
- **Headers**: Adjust the `remove_header` function to target different security headers.

## Disclaimer

This script is for educational purposes only. Performing man-in-the-middle attacks without permission is illegal. Use only on your own networks or with explicit consent. The author is not responsible for misuse.
