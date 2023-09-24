from scapy.all import *
import sys

def load_ports_from_file(filename):
    # Open the ports file and split the contents by comma
    with open(filename, 'r') as ports_file:
        ports = ports_file.read().split(",")
    # Convert the ports to integers and return as a list
    return [int(port) for port in ports]

def is_ping_reply(ping):
    # Check if ICMP packet type is 0 (Echo Reply)
    return ping[1][ICMP].type == 0

def is_tcp_synack(packet):
    # Check if TCP flags indicate a SYN-ACK packet
    return packet[1][TCP].flags != "SA"

def main():
    if len(sys.argv) != 2:
        # Display usage information if incorrect number of arguments
        print("Usage: python3 scanner.py <target>")
        sys.exit(1)

    target = sys.argv[1]

    print("[+] Stage: Host discovery")
    # Send ICMP Echo requests and collect responses
    pings, unans = sr(IP(dst=target)/ICMP(), timeout=2)

    hosts = []
    for ping in pings:
        if is_ping_reply(ping):
            # Add discovered host to the list
            hosts.append({
                "ip": ping[0].dst,
                "services": []
            })

    print("[+] Stage: Service discovery")

    nmap_top1000_int = load_ports_from_file("./nmap-top1000.txt")

    for host in hosts:
        for port in nmap_top1000_int:
            # Send TCP packets to discover open ports on the host
            tcp_result, unans = sr(IP(dst=host["ip"])/TCP(dport=port), timeout=1)
            print(f'Host: {host["ip"]}, Port: {port}')
            for tcp_conn in tcp_result:
                if is_tcp_synack(tcp_conn):
                    # Record open ports for the host
                    host["services"].append(tcp_conn[0][TCP].dport)
                    print(f"\t- Open port: {tcp_conn[0][TCP].dport}")

if __name__ == "__main__":
    main()
