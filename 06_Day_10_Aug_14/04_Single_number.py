def single_number(data):
    count = 0
    if len(data) == 1:
        count = 1
    else:
        for i in data:
            if data.count(i) > 1:
                count += 1
    return count


print(single_number([4, 1, 2, 1, 2]))
