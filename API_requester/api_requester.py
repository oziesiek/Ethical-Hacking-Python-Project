import tkinter as tk  # Import tkinter for GUI components
from tkinter import Text  # Import Text widget for displaying output
import requests  # Import requests for making API calls
import threading  # Import threading for concurrent execution
import colorama  # for colors
from colorama import Fore, Style

# Initialize colorama for terminal text coloring
colorama.init()

# Function to send GET requests to a specified endpoint
def send_get_request(endpoint):
    """Send a GET request to the specified endpoint and display the response."""
    output_text.delete(1.0, tk.END)  # Clear previous output
    try:
        response = requests.get(endpoint)  # Send a GET request
        formatted_response = f"{Fore.YELLOW}Endpoint:{Style.RESET_ALL} {endpoint}\n{Fore.GREEN}Status Code:{Style.RESET_ALL} {response.status_code}\n{Fore.GREEN}Response:{Style.RESET_ALL} {response.text}\n"
        output_text.insert(tk.END, formatted_response)  # Display the response
    except Exception as e:
        output_text.insert(tk.END, f"[X] An error occurred: {e}\n")  # Log any errors

def start_request():
    """Start the API request in a separate thread."""
    endpoint = endpoint_entry.get()  # Get the endpoint from the entry
    threading.Thread(target=send_get_request, args=(endpoint,)).start()  # Start the request in a new thread

def create_menu():
    """Create the main GUI menu for the API requester."""
    global output_text, endpoint_entry  # Declare output_text and endpoint_entry as global variables
    root = tk.Tk()  # Create the main window
    root.title("API Requester")  # Set the window title

    # Set the background color of the main window
    root.configure(bg="#778899")

    # Input Fields
    tk.Label(root, text="API Endpoint:", fg="white", bg="#778899").pack(pady=5)  # Label for endpoint
    endpoint_entry = tk.Entry(root, width=50)  # Entry for API endpoint
    endpoint_entry.pack(pady=5)  # Add padding

    # Button to start the request
    btn_request = tk.Button(root, text="Send Request", command=start_request, bg="#778899", fg="white")  # Button to send request
    btn_request.pack(pady=10)  # Add padding

    # Output Text Widget
    output_text = Text(root, height=20, width=80, bg="#2C3E50", fg="white", wrap="word")  # Create a Text widget for output
    output_text.pack(pady=10)  # Add padding

    root.mainloop()  # Start the GUI event loop

# Entry point of the program
if __name__ == "__main__":
    create_menu()  # Create the GUI menu
