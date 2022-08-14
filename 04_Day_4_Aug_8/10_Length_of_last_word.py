def length_of_last_word(s):
    result = []
    arr = s.split(" ")
    for i in arr:
        if i.isalpha():
            result.append(i)
    return len(result[len(result) - 1])


print(length_of_last_word("   fly me   to   the moon  "))
