def findMaxConsecutiveOnes(data):
    string = ''
    answer = []
    for i in range(len(data)):
        if data[i] == 1:
            string += str(data[i])
        else:
            string += " "

    answer = string.split(" ")
    return len(max(answer))


print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
# print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
