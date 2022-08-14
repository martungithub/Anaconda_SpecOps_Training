def sum_of_unique_elements(data):
    sum_of_elements = 0
    for i in range(len(data)):
        if data.count(data[i]) == 1:
            sum_of_elements += data[i]

    return sum_of_elements


print(sum_of_unique_elements([1, 2, 3, 2]))
# print(sum_of_unique_elements([1,2,3,4,5]))
# print(sum_of_unique_elements([1,1,1,1,1]))
