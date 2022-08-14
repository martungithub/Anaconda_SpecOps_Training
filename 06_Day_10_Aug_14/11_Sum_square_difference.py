def sum_of_squares(size):
    numbers = []
    square_of_the_sum = 0
    sum_of_the_squares = 0
    for i in range(size + 1):
        numbers.append(i)

    for i in numbers:
        square_of_the_sum += i ** 2
        sum_of_the_squares += i

    return sum_of_the_squares ** 2 - square_of_the_sum


print(sum_of_squares(100))
# print(sum_of_squares(100))
