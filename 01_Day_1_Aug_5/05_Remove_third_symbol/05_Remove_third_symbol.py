string = input("Insert the string: ")
result = string[0]
for i in range(1, len(string)):
    if i % 3 != 0:
        result += string[i]
print("Result: ", result)
