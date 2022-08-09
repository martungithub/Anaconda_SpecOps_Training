def f(n):
    a, b = 1, 1
    sum = 0
    for i in range(0, n):
        if a <= 4000000:
            a, b = b, a + b
            if a % 2 == 0:
                sum += a

    return sum


print(f(10))
