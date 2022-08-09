number = input("Enter the number: ")
sum_of_digits = 0
product = 1
for i in number:
    sum_of_digits += int(i)
    product *= int(i)
print("Difference of product and sum is: ", product - sum_of_digits)