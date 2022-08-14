import math


def is_prime(num):
    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True


def largest_prime_factor(number):
    answer = []
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i) is True:
            answer.append(i)
    return answer


print(max(largest_prime_factor(600851475143)))
