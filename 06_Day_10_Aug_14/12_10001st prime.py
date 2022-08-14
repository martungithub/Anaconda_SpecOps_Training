import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    count = 0
    result = 1

    while count < n:
        result += 1
        if is_prime(result):
            count += 1
    return result


print(find_prime(10001))
