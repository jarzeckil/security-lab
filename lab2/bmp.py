from Crypto.Cipher import AES


def generate_passwords():
    passwords = []
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
    for char in charset:
        password = (char * 16).encode('utf-8')
        passwords.append(password)

    return passwords

def decrypt_aes(key, text):
    aes = AES.new(key, AES.MODE_ECB)
    decrypted = aes.decrypt(text)

    return decrypted

def check_decryption(decrypted):
    if decrypted.startswith(b'BM'):
        return True
    return False

with open("lab2/security_ECB_encrypted.bmp", "rb") as f:
    text = f.read(16)

passwords = generate_passwords()

for p in passwords:
    decrypted = decrypt_aes(p, text)
    if check_decryption(decrypted):
        print(f"key is {p.decode('utf-8')}")
        break
