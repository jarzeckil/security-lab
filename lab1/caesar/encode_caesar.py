from unidecode import unidecode
def caesar(text, key):
    result = ""
    for i in range(len(text)):
        if(text[i].islower()):
            result += chr((ord(text[i]) - ord('a') + key)%26 + ord('a'))
        elif(text[i].isupper()):
            result += chr((ord(text[i]) - ord('A') + key)%26 + ord('A'))
        else:
            result += text[i]
    return result

def normalize_text(text):
    return unidecode(text)


with open("lab1/caesar/de.txt", "r") as f:
    text = f.read()
text = normalize_text(text)

text_encoded = caesar(text, 16)

with open("lab1/caesar/de_encoded_16.txt", "x") as f:
    f.write(text_encoded)



