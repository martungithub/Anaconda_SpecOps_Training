text = open("text.txt", "r")
modified = open("modified.txt", "w")
modified_word = ""
for line in text:
    for word in line.split(","):
        modified.write(word[0] + word[1].upper() + word[2:].lower() + " ")
text.close()
modified.close()