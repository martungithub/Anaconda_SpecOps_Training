text = open("symbols.txt", "r")
modified_word = ""
for line in text:
    for word in line:
        modified_word += word
text.close()
print("Number of characters: ", len(modified_word))
