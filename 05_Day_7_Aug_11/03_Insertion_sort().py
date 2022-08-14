def insertion_sort(data):
    for step in range(1, len(data)):
        key = data[step]
        j = step - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = key


print(insertion_sort([1, 4, 3, 2, 5, 7, 8, 6]))
