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

def decode(text, table):
    chars_count = Counter(c for c in text.lower() if c.isalpha())
    n = chars_count.total()

    p = {}

    for c in text:
        p[c] = chars_count[c]/n

    c_max = max(p, key=p.get)

    key = ord(c_max) - ord(max(table, key=table.get))

    key = key%26


    return key


with open("lab1/eng_encoded_24.txt", "r") as f:
    text = f.read()

print(decode(text, eng_table))
