from collections import Counter
import math

def create_keystream(key, N):
    S = [i for i in range(256)]

    j  = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i%len(key)])) % 256
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp

    i = 0
    j = 0
    keystream = []

    for _ in range(N):
        i = (i+1)%256
        j = (j+S[i]) % 256
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp
        keystream.append(S[(S[i]+S[j]) % 256])

    return keystream


def decipher_rc4(text, keystream):
    n = len(text)
    decoded = ""
    for i in range(n):
        decoded += chr(text[i] ^ keystream[i])
    
    return decoded

def calc_entropy(text):
    c = Counter(text)
    n = c.total()

    p = {}

    for char in c:
        p[char] = c[char]/n

    sum = 0

    for char in c:
        sum += p[char] * math.log(p[char])

    sum = -1 * sum

    return sum



with open("lab1/rc4/crypto2.rc4", "rb") as f:
    text = f.read()

with open("lab1/rc4/keys.txt", "r") as f:
    file = f.read()

keys = file.split()

keys_entropy = {}
N = len(text)

for key in keys:
    print(key)
    keystream = create_keystream(key, N)
    deciphered = decipher_rc4(text, keystream)
    keys_entropy[key] = calc_entropy(deciphered)

key = min(keys_entropy, key=keys_entropy.get)
keystream = create_keystream(key, N)
deciphered = decipher_rc4(text, keystream)
print(key)
print(deciphered)


#crypto.rc4 def
#crypto2.rc4 eac


