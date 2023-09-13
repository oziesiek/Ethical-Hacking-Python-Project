#!/usr/bin/env python

import subprocess
import optparse
import re

# Function to parse command-line arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC, use --help for more info.")
    return options

# Function to change the MAC address of a given interface
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])  # Disable the interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])  # Set the new MAC address
    subprocess.call(["ifconfig", interface, "up"])  # Enable the interface

# Function to get the current MAC address of a given interface
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()  # Get ifconfig output
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)  # Search for MAC address

    if mac_address_search_result:
        return mac_address_search_result.group(0)  # Return the found MAC address
    else:
        print("[-] Could not read MAC address.")  # Print error message if MAC address not found

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")  # Fix typo: "addres" to "address"
