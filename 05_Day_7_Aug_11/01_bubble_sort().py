def bubble_sort(data):
    for i in range(len(data) - 1):
        check = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                check = True

        if check == False:
            break
    return data


print(bubble_sort([1, 2, 4, 6, 5, 7]))
