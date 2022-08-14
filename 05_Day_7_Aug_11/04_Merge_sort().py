def sort(data1, data2):
    i = j = 0
    result = []
    while i < len(data1) and j < len(data2):
        if data1[i] < data2[j]:
            result.append(data1[i])
            i += 1
        else:
            result.append(data2[j])
            j += 1

    while j < len(data2):
        result.append(data2[j])
        j += 1

    while i < len(data1):
        result.append(data1[i])
        i += 1

    return result


def divide(data):
    if len(data) < 2:
        return data
    else:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        array1 = divide(left)
        array2 = divide(right)
        return sort(array1, array2)


print(divide([1, 3, 6, 5, 0, 4, 7, 8, 6]))
