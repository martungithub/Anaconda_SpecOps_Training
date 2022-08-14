def Degree_of_Array(data):
    count = 0
    repeated = []
    sub_arr = []
    answer = []
    num = []
    lengths = []
    for i in range(len(data)):
        count = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                count += 1
        repeated.append(count)

    for i in range(len(data)):
        if data.count(data[i]) == max(repeated) and data[i] not in num:
            num.append(data[i])

    for i in range(len(data) + 1):
        for j in range(i):
            sub_arr.append(data[j:i])

    for i in range(len(sub_arr)):
        for j in range(len(num)):
            if sub_arr[i].count(num[j]) == max(repeated):
                answer.append(sub_arr[i])

    for i in range(len(answer)):
        lengths.append(len(answer[i]))

    for i in range(len(lengths)):
        if len(answer[i]) == min(lengths):
            print(answer[i])


Degree_of_Array([1, 2, 2, 3, 1])
