def remove_dublicates(data):
    unique = []
    for i in data:
        if i not in unique:
            unique.append(i)
    unique.sort()
    return unique


print(remove_dublicates([1, 1, 2, 4, 4, 7, 8, 9, 5, 4, 1]))
