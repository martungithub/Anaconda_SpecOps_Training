def sort_array_by_bit_parity(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] % 2 != 0:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


print(sort_array_by_bit_parity([7, 8, 6, 5]))
