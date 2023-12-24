import pikepdf
from tqdm import tqdm
import colorama  # for colors
from colorama import Fore, Style

# Initialize colorama
colorama.init()

def print_ftp_banner():
    # Function to print a colorful banner
    banner = r"""
    __________________   _____                _             
    | ___ \  _  \  ___| /  __ \              | |            
    | |_/ / | | | |_    | /  \/_ __ __ _  ___| | _____ _ __ 
    |  __/| | | |  _|   | |   | '__/ _` |/ __| |/ / _ \ '__|
    | |   | |/ /| |     | \__/\ | | (_| | (__|   <  __/ |   
    \_|   |___/ \_|      \____/_|  \__,_|\___|_|\_\___|_| by Oziesiek   
    """
    colored_banner = f"{Fore.RED}{banner}{Style.RESET_ALL}"
    print(colored_banner)

# Call the function to print the FTP banner
print_ftp_banner()

# Load password list
pdf_file = input("\nProvide .pdf file: ")
wordlist = input("Provide wordlist .txt file: ")
passwords = [line.strip() for line in open(wordlist)]

# Iterate over passwords
def main():
    for password in tqdm(passwords, "Decrypting PDF"):
        try:
            # open PDF file
            with pikepdf.open(pdf_file, password=password) as pdf:
                # Password decrypted successfully, break out of the loop
                print(f"\n{Fore.YELLOW}[+] Password found:{Style.RESET_ALL} {Fore.RED}{password}{Style.RESET_ALL}")
                break
        except pikepdf._core.PasswordError as e:
            # wrong password, just continue in the loop
            continue

if __name__ == "__main__":
    # Call the main function
    main()
    input("Press Enter to exit...")
