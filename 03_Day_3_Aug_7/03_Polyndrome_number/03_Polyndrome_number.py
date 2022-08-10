def polyndrome(number):
    divisor = 1
    new_number = 0
    initial_number = number
    k = len(str(number)) - 1
    while divisor != 0:
        divisor = number % 10
        number = number // 10
        new_number += 10 ** k * divisor
        k -= 1
    if initial_number == int(new_number):
        return True
    else:
        return False


print(polyndrome(121))
