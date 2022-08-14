def Insertion_of_Array(list1, list2):
    unique = []
    answer = []
    for i in list1:
        if i not in unique:
            unique.append(i)
    for j in list2:
        if j not in unique:
            unique.append(j)
    for i in unique:
        if i in list1 and i in list2:
            answer.append(i)

    return answer


print(Insertion_of_Array([1, 2, 2, 3, 5], [2, 2, 3, 6]))
