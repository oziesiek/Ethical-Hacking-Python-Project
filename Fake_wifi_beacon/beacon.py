# Import necessary modules
from scapy.all import *
from threading import Thread
from faker import Faker

# Function to send beacon frames
def send_beacon(ssid, mac, infinite=True):
    # Hardcoded MAC address for the sender
    sender_mac = "YOUR MAC ADDRES"

    # Create Dot11 frame for beacon
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)

    # Create Beacon frame with ESS+privacy capability
    beacon = Dot11Beacon(cap="ESS+privacy")

    # Create SSID element in the frame
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))

    # Construct the frame with RadioTap header
    frame = RadioTap() / dot11 / beacon / essid

    # Send the frame using Scapy
    sendp(frame, inter=0.1, loop=1, iface=iface, verbose=0)

# Main part of the script
if __name__ == "__main__":
    # Number of access points to simulate
    n_ap = 5

    # Network interface name
    iface = "wlan0"

    # Generate random SSIDs and MACs using Faker
    faker = Faker()
    ssids_macs = [(faker.name(), faker.mac_address()) for i in range(n_ap)]

    # Start threads to send beacon frames for each simulated access point
    for ssid, mac in ssids_macs:
        Thread(target=send_beacon, args=(ssid, mac)).start()
