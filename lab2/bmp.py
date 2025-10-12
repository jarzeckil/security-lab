from Crypto.Cipher import AES

def decrypt_aes(key, text):
    aes = AES.new(key, AES.MODE_ECB)
    decrypted = aes.decrypt(text)

    return decrypted

def check_decryption(text):
    if(text[0] == 'B' and text[1] == 'M'):
        return True
    return False

with open("lab2/security_ECB_encrypted.bmp", "rb") as f:
    file = f.read(16)
