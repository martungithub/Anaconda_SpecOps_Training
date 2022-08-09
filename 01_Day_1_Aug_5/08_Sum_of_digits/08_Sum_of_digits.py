number = input("Enter the number: ")
sum_of_digits = 0
for i in number:
    sum_of_digits += int(i)
print(f'Sum of digits of {number} is: {sum_of_digits}')