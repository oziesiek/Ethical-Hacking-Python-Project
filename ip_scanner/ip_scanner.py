#!/usr/bin/env python
import argparse
import scapy.all as scapy

# Function to parse command-line arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options = parser.parse_args()

    if not options.target:
        parser.error("You must specify a target IP address or IP range.")
    return options

# Function to scan a target IP or IP range for connected devices
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # Create an ARP request packet for the target IP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Create an Ethernet frame with a broadcast MAC address
    arp_request_broadcast = broadcast/arp_request  # Combine the Ethernet frame and ARP request

    # Send the ARP request and receive responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        # Extract and store IP and MAC addresses in a dictionary
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

# Function to print the scan results
def print_result(results_lists):
    print("IP\t\t\tMAC Address\n-----------------------------------------------------------------------------")
    for client in results_lists:
        print(client["IP"] + "\t\t" + client["MAC"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
