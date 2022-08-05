text = open("text.txt", "r")
modified = open("modified.txt", "w")
modified_word = ""
for line in text:
    for word in line.split(" "):
        modified.write(word[0].upper() + word[1:] + " ")
text.close()
modified.close()