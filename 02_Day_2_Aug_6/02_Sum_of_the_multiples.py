sum_of_multiples = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_multiples += i

print("Sum of multiples: ", sum_of_multiples)
