def strStr(haystack, needle):
    possition = -1
    for i in haystack:
        if needle in haystack:
            haystack = haystack.replace(needle, ".")

    for i in range(len(haystack)):
        if haystack[i] == ".":
            possition = i

    return possition


print(strStr("hello", "o"))
