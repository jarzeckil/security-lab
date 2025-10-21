from passlib.hash import md5_crypt
import requests

passwds = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10k-most-common.txt").text.split()

salt = "a"

hashes = dict()

for passwd in passwds:
    hashed = md5_crypt.hash(passwd, salt=salt)
    hashed_head = hashed[:6]

    if(hashes.__contains__(hashed_head)):
        print(f"found pair: {hashes[hashed_head]} and {passwd}")
        print(f"full hashes: {md5_crypt.hash(hashes[hashed_head], salt=salt)} and {hashed}")
        break
    else:
        hashes[hashed_head] = passwd