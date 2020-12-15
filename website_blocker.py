import time
from datetime import datetime as dt

def block_during_hours(websites: list, start_hour: int, end_hour):
    hosts_path = r"/etc/hosts"
    hosts_temp = "hosts"
    redirect = "127.0.0.1"
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_hour):
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in websites:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
        else:
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in web_sites_list):
                        file.write(line)
                file.truncate()
            time.sleep(5)

if __name__ == "__main__":
    block_during_hours(["facebook.com", "instagram.com"], 9, 14)
