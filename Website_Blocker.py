import time
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = "127.0.0.1"

websites_input = input("Enter Websites to be blocked during Work Hours SEPARATED BY COMMA: ")
websites = websites_input.split(",")

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(host_path, "r+") as file:
            content = file.read()
            for web in websites:
                if web in content:
                    pass
                else:
                    file.write(redirect + " " + web + "\n")

        print("Work Hours...")

    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (web in line for web in websites):
                    file.write(line)
            file.truncate()
    
        print("Fun Hours...")
    time.sleep(5)

