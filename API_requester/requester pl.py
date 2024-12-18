import requests
import colorama  # do kolorów
from colorama import Fore, Style

# Inicjalizacja colorama dla kolorowania tekstu w terminalu
colorama.init()

# Funkcja do wyświetlania kolorowego banera
def print_ftp_banner():
    banner = r"""
    ___    ____  ____   ____                             __           
   /   |  / __ \/  _/  / __ \___  ____ ___  _____  _____/ /____  _____
  / /| | / /_/ // /   / /_/ / _ \/ __ `/ / / / _ \/ ___/ __/ _ \/ ___/
 / ___ |/ ____// /   / _, _/  __/ /_/ / /_/ /  __(__  ) /_/  __/ /    
/_/  |_/_/   /___/  /_/ |_|\___/\__, /\__,_/\___/____/\__/\___/_/     
                                  /_/                                                              
    """
    colored_banner = f"{Fore.CYAN}{banner}{Style.RESET_ALL}"
    print(colored_banner) 

# Wywołanie funkcji, aby wyświetlić baner
print_ftp_banner()                                                                                  

# Funkcja do wysyłania żądań GET na podany endpoint z listą wywołań
def send_get_request(endpoint, call_list):
    responses = []
    for call in call_list:
        # Konstrukcja URL dla każdego wywołania
        url = f"{endpoint}/{call.strip()}"
        # Wysyłanie żądania GET
        response = requests.get(url)
        # Dodanie szczegółów odpowiedzi do listy
        responses.append((call, response.status_code, response.text))
    return responses

# Funkcja do zapisywania odpowiedzi do pliku
def save_responses(responses, output_file):
    with open(output_file, 'w') as file:
        for call, status_code, data in responses:
            # Zapisanie każdej odpowiedzi do pliku
            file.write(f"{call}: {status_code} - {data}\n")

# Funkcja do formatowania i kolorowania odpowiedzi dla lepszego wyświetlania
def format_response(call, status_code, data):
    formatted_response = f"{Fore.YELLOW}{call}:{Style.RESET_ALL} {Fore.GREEN}{status_code}{Style.RESET_ALL} - {data}"
    return formatted_response

# Główna funkcja do uruchomienia skryptu
def main():
    # Pobranie od użytkownika adresu API
    endpoint = input(f"{Fore.RED}Podaj adres API:{Style.RESET_ALL} ")

    # Pytanie użytkownika, czy chce podać plik z listą wywołań, czy pojedynczą wartość
    option = input(f"Czy chcesz podać plik zawierający listę wywołań API (np. 'call1', 'call2', itp.)? {Fore.RED}(T/N){Style.RESET_ALL}: ").strip().lower()

    if option == 't':
        # Jeśli użytkownik chce podać plik, pobierz nazwę pliku
        filename = input(f"Podaj nazwę pliku .txt z listą wywołań{Fore.CYAN} (Naciśnij Enter, aby pominąć):{Style.RESET_ALL} ")
        if not filename:
            # Jeśli nie podano nazwy pliku, poproś o pojedyncze wywołanie
            single_request = input("Podaj wartość do wykonania pojedynczego wywołania: ").strip()
            call_list = [single_request] if single_request else []
        else:
            # Odczytaj listę wywołań z pliku
            with open(filename, 'r') as file:
                call_list = file.readlines()
    else:
        # Jeśli użytkownik nie chce podać pliku, poproś o pojedyncze wywołanie
        single_request = input("Podaj wywołanie do wykonania pojedynczego żądania: ").strip()
        call_list = [single_request] if single_request else []

    # Wysyłanie żądań GET
    responses = send_get_request(endpoint, call_list)

    # Pytanie użytkownika, czy chce zapisać odpowiedzi do pliku, czy wyświetlić na ekranie
    output_file = input(f"Podaj nazwę pliku wyjściowego {Fore.CYAN}(Naciśnij Enter, aby wyświetlić na ekranie):{Style.RESET_ALL} ")
    if output_file:
        # Jeśli podano nazwę pliku, zapisz odpowiedzi do pliku
        save_responses(responses, output_file)
        print(f"Odpowiedzi zapisane do pliku {Fore.YELLOW}{output_file}{Style.RESET_ALL}")
    else:
        # Jeśli nie podano nazwy pliku, wyświetl odpowiedzi na ekranie
        for call, status_code, data in responses:
            formatted_response = format_response(call, status_code, data)
            print(formatted_response)

# Punkt wejściowy do uruchomienia skryptu
if __name__ == "__main__":
    # Wywołanie funkcji main
    main()
    while True:
        # Pytanie użytkownika, czy chce wykonać kolejne wywołanie
        another_call = input(f"Czy chcesz wykonać kolejne wywołanie? {Fore.RED}(T/N){Style.RESET_ALL}: ").strip().lower()
        if another_call == 't':
            main()
