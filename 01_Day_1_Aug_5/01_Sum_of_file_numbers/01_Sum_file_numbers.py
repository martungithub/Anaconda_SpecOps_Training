f = open("numbers.txt", "r")
numbers = f.readline().split(",")
f.close()
sum_of_numbers = 0
for i in numbers:
    sum_of_numbers += int(i)
print("Sum of numbers: ", sum_of_numbers)