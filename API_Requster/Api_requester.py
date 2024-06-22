import requests
import colorama  # for colors
from colorama import Fore, Style

# Initialize colorama for terminal text coloring
colorama.init()

# Function to print a colorful banner
def print_ftp_banner():
    banner = r"""
    ___    ____  ____   ____                             __           
   /   |  / __ \/  _/  / __ \___  ____ ___  _____  _____/ /____  _____
  / /| | / /_/ // /   / /_/ / _ \/ __ `/ / / / _ \/ ___/ __/ _ \/ ___/
 / ___ |/ ____// /   / _, _/  __/ /_/ / /_/ /  __(__  ) /_/  __/ /    
/_/  |_/_/   /___/  /_/ |_|\___/\__, /\__,_/\___/____/\__/\___/_/     
                                  /_/ by Oziesiek                                                             
    """
    colored_banner = f"{Fore.CYAN}{banner}{Style.RESET_ALL}"
    print(colored_banner) 

# Call the function to print the banner
print_ftp_banner()                                                                                  

# Function to send GET requests to a specified endpoint with a list of calls
def send_get_request(endpoint, call_list):
    responses = []
    for call in call_list:
        # Construct the URL for each call
        url = f"{endpoint}/{call.strip()}"
        # Send a GET request
        response = requests.get(url)
        # Append the response details to the list
        responses.append((call, response.status_code, response.text))
    return responses

# Function to save responses to a file
def save_responses(responses, output_file):
    with open(output_file, 'w') as file:
        for call, status_code, data in responses:
            # Write each response to the file
            file.write(f"{call}: {status_code} - {data}\n")

# Function to format and colorize a response for better display
def format_response(call, status_code, data):
    formatted_response = f"{Fore.YELLOW}{call}:{Style.RESET_ALL} {Fore.GREEN}{status_code}{Style.RESET_ALL} - {data}"
    return formatted_response

# Main function to execute the script
def main():
    # Get the API endpoint from the user
    endpoint = input(f"{Fore.RED}Enter the API endpoint:{Style.RESET_ALL} ")

    # Ask the user if they want to provide a file or a single custom value
    option = input(f"Do you want to provide a file containing a list of API calls (e.g., 'call1', 'call2', etc.)? {Fore.RED}(Y/N){Style.RESET_ALL}: ").strip().lower()

    if option == 'y':
        # If the user wants to provide a file, get the filename
        filename = input(f"Provide .txt filename with the list of calls to be made{Fore.CYAN} (Press Enter to skip):{Style.RESET_ALL} ")
        if not filename:
            # If no filename is provided, ask for a single custom request
            single_request = input("Enter the input to make a single request: ").strip()
            call_list = [single_request] if single_request else []
        else:
            # Read the list of calls from the file
            with open(filename, 'r') as file:
                call_list = file.readlines()
    else:
        # If the user doesn't want to provide a file, ask for a single custom request
        single_request = input("Enter the call to make a single request: ").strip()
        call_list = [single_request] if single_request else []

    # Send GET requests
    responses = send_get_request(endpoint, call_list)

    # Ask the user if they want to save responses to a file or display on the screen
    output_file = input(f"Enter the output file name {Fore.CYAN}(Press Enter to display it on screen):{Style.RESET_ALL} ")
    if output_file:
        # If a filename is provided, save responses to the file
        save_responses(responses, output_file)
        print(f"Responses saved to {Fore.YELLOW}{output_file}{Style.RESET_ALL}")
    else:
        # If no filename is provided, display responses on the screen
        for call, status_code, data in responses:
            formatted_response = format_response(call, status_code, data)
            print(formatted_response)

# Entry point to run the script
if __name__ == "__main__":
    # Call the main function
    main()
    while True:
        # Ask the user if they want to make another call
        another_call = input(f"Do you want to make another call? {Fore.RED}(Y/N){Style.RESET_ALL}: ").strip().lower()
        if another_call == 'y':
            main()
        else:
            print("Exiting the program.")
            break
