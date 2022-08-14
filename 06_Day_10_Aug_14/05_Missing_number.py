def missing_number(data):
    n = len(data)
    answer = 0
    for i in range(n):
        if i not in data:
            answer = i
    return answer


# print(missing_number([3,0,1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
