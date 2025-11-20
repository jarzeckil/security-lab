import client as cli
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

client = cli.Client('http://10.42.12.232:5555')

with open('key.txt', 'rb') as f:
    key_text = f.read()

rsa_keys = RSA.import_key(key_text)

messages = client.get_binary_message('331697')

decipher = PKCS1_OAEP.new(rsa_keys)
print(decipher.decrypt(messages))



recipient_uid = '331736'
recipient_key = RSA.import_key(client.get_key(recipient_uid))

cipher = PKCS1_OAEP.new(recipient_key)
encrypted = cipher.encrypt(b"pawelek tez jest spoko")

client.send_binary_message(recipient_uid, encrypted)
