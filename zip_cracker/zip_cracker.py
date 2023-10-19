import zipfile

# Open the dictionary file containing passwords
with open('darkweb2017-top10000.txt', 'r', encoding='utf-8') as text:
    # Read each line (password) from the dictionary file
    for entry in text.readlines():
        # Encode the password as bytes
        password = entry.strip().encode('utf-8')
        
        try:
            # Try to extract the protected zip file using the current password
            with zipfile.ZipFile('you_protected_file.zip', 'r') as zf:
                # Attempt to extract files using the provided password
                zf.extractall(pwd=password)
                
                # Get the name and size of the first extracted file
                data = zf.namelist()[0]
                data_size = zf.getinfo(data).file_size
                
                # Print success message with the found password and extracted file details
                print('**********')
                print('[+] Password found: {}'.format(password.decode('utf-8')))
                print('[+] Extracted File: {}'.format(data))
                print('[+] File Size: {} bytes'.format(data_size))
                print('**********')
                
                # Break the loop since the correct password is found
                break
        # Handle specific exceptions that occur when a bad password is provided
        except (RuntimeError, zipfile.BadZipFile, NotImplementedError):
            # Ignore exceptions and continue searching for the correct password
            pass
