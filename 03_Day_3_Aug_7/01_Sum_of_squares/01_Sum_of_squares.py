sum_of_square = 0
sum_square = 0
for i in range(0, 101):
    sum_square += i
    sum_of_square += i * i

print("Difference: ", sum_square * sum_of_square - sum_of_square)
