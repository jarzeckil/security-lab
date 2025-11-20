import client as cli
from Crypto.PublicKey import RSA

client = cli.Client('http://10.42.12.232:5555')

rsa_keys = RSA.generate(1024)
pub_key = rsa_keys.public_key()

client.send_key('331697', pub_key.export_key())

with open('key.txt', 'wb') as f:
    f.write(rsa_keys.export_key())