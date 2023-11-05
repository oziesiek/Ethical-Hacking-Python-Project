import subprocess
import os
import re
from collections import namedtuple
import configparser

# Function to retrieve saved SSIDs in a Windows machine
def get_windows_saved_ssids():
    """Returns a list of saved SSIDs in a Windows machine using netsh command"""
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s+:\s(.*)", output)
    for profile in profiles:
        ssid = profile.strip()
        ssids.append(ssid)
    return ssids

# Function to extract saved Wi-Fi passwords from Windows
def get_windows_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords saved in a Windows machine using netsh command"""
    ssids = get_windows_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"], defaults=("", "", ""))
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(f'netsh wlan show profile name="{ssid}" key=clear').decode()
        ciphers = re.findall(r"Cipher\s+:\s(.*)", ssid_details)
        ciphers = "/".join([c.strip() for c in ciphers])
        key = re.findall(r"Key Content\s+:\s(.*)", ssid_details)
        try:
            key = key[0].strip()
        except IndexError:
            key = "None"
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        if verbose >= 1:
            print_windows_profiles(profile)
        profiles.append(profile)
    return profiles

# Function to print Windows Wi-Fi profiles
def print_windows_profiles(profile):
    """Prints the Windows Wi-Fi profiles"""
    print(f"{profile.ssid:<25} {profile.ciphers:<15} {profile.key}")

# Function to extract saved Wi-Fi passwords in Linux
def get_linux_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords in Linux from /etc/NetworkManager/system-connections/ directory"""
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth_alg", "key_mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields], defaults=("", "", "", ""))
    profiles = []
    for file in os.listdir(network_connections_path):
        data = {k.replace("-", "_"): None for k in fields}
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v
        profile = Profile(**data)
        if verbose >= 1:
            print_linux_profiles(profile)
        profiles.append(profile)
    return profiles

# Function to print Linux Wi-Fi profiles
def print_linux_profiles(profile):
    """Prints the Linux Wi-Fi profiles"""
    ssid = profile.ssid if profile.ssid else ""
    auth_alg = profile.auth_alg if profile.auth_alg else ""
    key_mgmt = profile.key_mgmt if profile.key_mgmt else ""
    psk = profile.psk if profile.psk else ""
    print(f"{ssid:<25} {auth_alg:<15} {key_mgmt:<15} {psk}")

# Main function to select the operating system and retrieve Wi-Fi passwords
def main():
    print("Select the operating system:")
    print("1. Windows")
    print("2. Linux")
    choice = input("Enter your choice: ")

    if choice == "1":
        get_windows_saved_wifi_passwords()
    elif choice == "2":
        get_linux_saved_wifi_passwords()
    else:
        print("Invalid choice. Please select 1 for Windows or 2 for Linux.")

if __name__ == "__main__":
    main()
