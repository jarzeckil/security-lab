import client as cli
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = cli.Client('http://10.42.12.232:5555')

pub_key_deadbeef = RSA.import_key(client.get_key('deadbeef'))

cipher = PKCS1_OAEP.new(pub_key_deadbeef)
encrypted = cipher.encrypt(b"lol")

client.send_binary_message('deadbeef', encrypted)


