import socket
import ipaddress
import threading

def scan_port(ip, port, open_ports):
    """Scans a single port on a given host"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass

def scan_host(ip, ports_to_scan):
    """Scans all ports on a given host"""
    open_ports = []
    threads = []
    
    for port in ports_to_scan:
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    if open_ports:
        print(f"\nHost {ip} is active")
        print(f"Open ports: {open_ports}")

def main():
    while True:
        # Get user input
        target = input("Enter IP address or network range (e.g., 192.168.1.0/24): ")
        
        # Get port scanning preference
        port_choice = input("Do you want to scan only well-known ports (Y/N)? ").upper()
        
        if port_choice == 'Y':
            ports_to_scan = range(1, 1025)  # Well-known ports
        else:
            try:
                start_port = int(input("Enter start port number: "))
                end_port = int(input("Enter end port number: "))
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    raise ValueError("Invalid port range")
                ports_to_scan = range(start_port, end_port + 1)
            except ValueError as e:
                print(f"Error: Invalid port range - {e}")
                continue
        
        try:
            # Check if it's a single IP address or network range
            if '/' in target:
                network = ipaddress.ip_network(target, strict=False)
                print(f"\nScanning network {network}")
                for ip in network.hosts():
                    scan_host(str(ip), ports_to_scan)
            else:
                # Scanning single IP address
                print(f"\nScanning host {target}")
                scan_host(target, ports_to_scan)
                
        except ValueError as e:
            print(f"Error: Invalid IP address or network range format - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        # Ask if user wants to scan another target
        another_scan = input("\nDo you want to scan another target? (Y/N): ").upper()
        if another_scan != 'Y':
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()