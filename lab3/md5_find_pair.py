from hashlib import md5


with open("lab3/passwords.txt", "r") as f:
    file = f.read()

passwds = file.split()

hashes = dict()

for passwd in passwds:

    encoded_passwd = passwd.encode('utf-8')

    hashed = md5(encoded_passwd)

    hashed_head = hashed.hexdigest()[:6]

    if(hashed_head in hashes):
        print(f"found pair: {hashes[hashed_head]} and {passwd}")
        print(f"full hashes: {md5(hashes[hashed_head].encode('utf-8')).hexdigest()} and {hashed.hexdigest()}")
        break
    else:
        hashes[hashed_head] = passwd
