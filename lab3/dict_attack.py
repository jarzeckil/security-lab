from passlib.hash import md5_crypt, argon2, sha256_crypt
import requests

passwds = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10k-most-common.txt").text.split()

hash_md5 = "$1$k8nhEGc9$MwWuWMnHqzGdszCwI98RZ0"
hash_sha256 = "$5$rounds=10000$ujmXZ4IqnXl.Bplf$4lcwpQwc.kZFIuCrV8Mgg8bP.Mv.jxx9NitjrqQPK8/"
hash_argon2 = "$argon2id$v=19$m=65536,t=3,p=4$GWMMQYgxJmQshdB6L0UIgQ$+glO5pBsNQ6Fb80yakwkzUfSXdX9nQM0ygF2ZNJ5DwI"
hash_md5_pepper = "$1$o8ZWp.W5$FIkSXN.lufeIWvllfQW9l1"


for passwd in passwds:
    print(passwd)
    md5_check = md5_crypt.hash(passwd, salt="")
    if(md5_check == hash_md5):
        print(f"passwd is {passwd}")
        break

