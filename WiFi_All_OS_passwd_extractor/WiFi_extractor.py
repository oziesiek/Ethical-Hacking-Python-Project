import subprocess
import os
import re
from collections import namedtuple
import platform
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

# Function to retrieve saved SSIDs in a macOS machine
def get_macos_saved_ssids():
    """Returns a list of saved SSIDs in macOS using security command"""
    output = subprocess.check_output(["security", "find-generic-password", "-D", "AirPort", "-g"]).decode()
    ssids = re.findall(r"\"ssid\"<blob>=(.*?)\n", output, re.DOTALL)
    return ssids

# Function to extract saved Wi-Fi passwords from macOS
def get_macos_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords in macOS using security command"""
    ssids = get_macos_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "password"], defaults=("", ""))
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(["security", "find-generic-password", "-D", "AirPort", "-l", ssid, "-w"]).decode().strip()
        profile = Profile(ssid=ssid, password=ssid_details)
        if verbose >= 1:
            print_macos_profiles(profile)
        profiles.append(profile)
    return profiles

# Function to print macOS Wi-Fi profiles
def print_macos_profiles(profile):
    """Prints the macOS Wi-Fi profiles"""
    print(f"{profile.ssid:<25} {profile.password}")

# Main function to select the operating system and retrieve Wi-Fi passwords
def main():
    print("Select the operating system:")
    print("1. Windows")
    print("2. Linux")
    print("3. macOS")
    choice = input("Enter your choice: ")

    if choice == "1" and platform.system() == "Windows":
        get_windows_saved_wifi_passwords()
    elif choice == "2" and platform.system() == "Linux":
        get_linux_saved_wifi_passwords()
    elif choice == "3" and platform.system() == "Darwin":
        get_macos_saved_wifi_passwords()
    else:
        print("Invalid choice or unsupported operating system.")

if __name__ == "__main__":
    main()
