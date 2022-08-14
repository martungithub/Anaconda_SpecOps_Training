def array_partition(data):
    data.sort()
    sum_of_pairs = 0
    for i in range(0, len(data), 2):
        sum_of_pairs += data[i]
    return sum_of_pairs


print(array_partition([6, 2, 6, 5, 1, 2]))
