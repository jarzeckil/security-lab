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


with open("lab1/eng.txt", "r") as f:
    text = f.read()

text_encoded = caesar(text, 5)

with open("lab1/eng_encoded_24.txt", "x") as f:
    f.write(text_encoded)




