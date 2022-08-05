text = open("symbols.txt", "r")
characters = ""
for line in text:
    for word in line:
        characters += word
text.close()
print("Number of characters: ", len(characters))
