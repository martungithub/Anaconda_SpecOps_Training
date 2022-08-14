def isPalindrome(num):
    return str(num) == str(num)[::-1]


def largest(number):
    mult = 0
    for i in range(number, 100, -1):
        for j in range(number, 100, -1):
            if isPalindrome(i * j):
                if i * j > mult:
                    mult = i * j
    return mult


print(largest(999))
