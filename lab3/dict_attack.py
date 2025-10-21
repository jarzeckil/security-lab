from passlib.hash import md5_crypt, argon2, sha256_crypt
import requests
import base64
import string

passwds = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10k-most-common.txt").text.split()

hash_md5 = "$1$k8nhEGc9$MwWuWMnHqzGdszCwI98RZ0"
hash_sha256 = "$5$rounds=10000$ujmXZ4IqnXl.Bplf$4lcwpQwc.kZFIuCrV8Mgg8bP.Mv.jxx9NitjrqQPK8/"
hash_argon2 = "$argon2id$v=19$m=65536,t=3,p=4$GWMMQYgxJmQshdB6L0UIgQ$+glO5pBsNQ6Fb80yakwkzUfSXdX9nQM0ygF2ZNJ5DwI"
hash_md5_pepper = "$1$o8ZWp.W5$FIkSXN.lufeIWvllfQW9l1"


for passwd in passwds:
    md5_check = md5_crypt.using(salt="k8nhEGc9").hash(passwd)
    if(md5_check == hash_md5):
        print(f"md5 passwd is {passwd}")
        break

for passwd in passwds:
    sha256_check = sha256_crypt.using(rounds=10000, salt="ujmXZ4IqnXl.Bplf").hash(passwd)
    if(sha256_check == hash_sha256):
        print(f"sha256 passwd is {passwd}")
        break

for passwd in passwds:
    print(passwd)
    argon2_check = argon2.using(memory_cost=65536, time_cost=3, max_threads=4, salt=base64.b64decode("GWMMQYgxJmQshdB6L0UIgQ"+"==")).hash(passwd)
    if(argon2_check == hash_argon2):
        print(f"argon2 passwd is {passwd}")
        break  

end = False
for passwd in passwds:
    for c in string.ascii_lowercase:
        md5_pepper_check = md5_crypt.using(salt="o8ZWp.W5").hash(passwd+c)
        if(md5_pepper_check == hash_md5_pepper):
            print(f"md5 passwd is {passwd}")
            end = True
            break
    if(end):
        break

