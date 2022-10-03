text = input()
newtext = ""

for letter in range(len(text), 0, -1):
    newtext += text[letter-1]

print(newtext)
