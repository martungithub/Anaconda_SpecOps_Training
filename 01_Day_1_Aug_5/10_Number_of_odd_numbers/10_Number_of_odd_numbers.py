a = int(input("Insert interval a: "))
b = 0
while a >= b:
    b = int(input("Insert interval b(b > a): "))
count = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        count += 1
print("Number of odd elements: ", count)
