fh = open("words.txt")
words = fh.readline().split()
for word in words:
    count = 0
    for word1 in words:
        if word == word1:
            count += 1
            words.remove(word)
    print(word, "--->", count)
