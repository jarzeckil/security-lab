from collections import Counter

eng_table = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.361,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074
}

pl_table = {
  "a": 8.91,
  "ą": 0.99,
  "b": 1.47,
  "c": 3.96,
  "ć": 0.40,
  "d": 3.25,
  "e": 7.66,
  "ę": 1.11,
  "f": 0.30,
  "g": 1.42,
  "h": 1.08,
  "i": 8.21,
  "j": 2.28,
  "k": 3.51,
  "l": 2.10,
  "ł": 1.82,
  "m": 2.80,
  "n": 5.52,
  "ń": 0.20,
  "o": 7.75,
  "ó": 0.85,
  "p": 3.13,
  "q": 0.14,
  "r": 4.69,
  "s": 4.32,
  "ś": 0.66,
  "t": 3.98,
  "u": 2.50,
  "v": 0.04,
  "w": 4.65,
  "x": 0.02,
  "y": 3.76,
  "z": 5.64,
  "ź": 0.06,
  "ż": 0.83
}

de_table = {
  "a": 5.58,
  "ä": 0.54,
  "b": 1.96,
  "c": 3.16,
  "d": 4.98,
  "e": 16.93,
  "f": 1.49,
  "g": 3.02,
  "h": 4.98,
  "i": 8.02,
  "j": 0.24,
  "k": 1.32,
  "l": 3.60,
  "m": 2.55,
  "n": 10.53,
  "o": 2.24,
  "ö": 0.30,
  "p": 0.67,
  "q": 0.02,
  "r": 6.89,
  "s": 6.42,
  "ß": 0.37,
  "t": 5.79,
  "u": 3.83,
  "ü": 0.65,
  "v": 0.84,
  "w": 1.78,
  "x": 0.05,
  "y": 0.05,
  "z": 1.21
}


def find_key(text, table):
    chars_count = Counter(c for c in text.lower() if c.isalpha())
    n = chars_count.total()

    p = {}

    for c in text:
        p[c] = chars_count[c]/n

    c_max = max(p, key=p.get)

    key = ord(c_max) - ord(max(table, key=table.get))

    key = key%26

    return key

def decode(text, key):
    result = ""
    for i in range(len(text)):
        if(text[i].islower()):
            result += chr((ord(text[i]) - ord('a') - key)%26 + ord('a'))
        elif(text[i].isupper()):
            result += chr((ord(text[i]) - ord('A') - key)%26 + ord('A'))
        else:
            result += text[i]
    return result


with open("lab1/caesar/de_encoded_2.txt", "r") as f:
    text = f.read()

key = find_key(text, de_table)
print(key)
print(decode(text, key))
