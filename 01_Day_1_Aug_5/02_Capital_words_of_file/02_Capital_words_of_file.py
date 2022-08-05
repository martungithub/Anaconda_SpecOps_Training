text = open("text.txt", "r")
modified = open("modified.txt", "w")
modified_word = ""
for line in text:
    for word in line.split(" "):
        if len(word) >= 3:
            modified.write(word[:2] + word[2].upper() + word[3:] + " ")
        elif len(word) == 3:
            modified.write(word[:1] + word[2].upper() + " ")
        else:
            modified.write(word + " ")
text.close()
modified.close()