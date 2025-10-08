keys = []

for a in range(ord('a'), ord('z')+1):
    for b in range(ord('a'), ord('z')+1):
        for c in range(ord('a'), ord('z')+1):
            keys.append(chr(a)+chr(b)+chr(c))
    

print(len(keys))


with open("lab1/keys.txt", "x") as f:
    for t in keys:
        f.write(t + "\n")
