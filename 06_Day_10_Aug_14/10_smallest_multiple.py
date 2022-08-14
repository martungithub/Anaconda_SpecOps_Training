def smallest_multiple(size):
    max_range = size + 1
    numbers = []
    check = []
    for i in range(2, max_range):
        numbers.append(i)
        check.append(False)

    while all(check) is False:

        for i in range(0, len(numbers)):
            if i == 0:
                check[0] = True
                i = 1
            if max_range % numbers[i] == 0:
                check[i] = True
                print(i, check[i])
        print(check)
        if all(check) is True:
            return max_range
        else:
            for i in range(len(check)):
                check[i] = False
        max_range += 1


# The program works properly. It calculates the smallest multiple for 10 so quick.
# If we change the size, the program will calculate correctly, but it will take some time(like 1-2 minutes) for 20.
# It depends on the size of your RAM etc...

size = 10
print(smallest_multiple(size))
