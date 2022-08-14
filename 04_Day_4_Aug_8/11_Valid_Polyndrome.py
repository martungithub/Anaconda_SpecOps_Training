def valid_polyndrome(s):
    new = ""
    original = ""
    for i in s:
        if i.isalpha():
            new += i.lower()
            original += i.lower()

    new = new[::-1]
    if new == original:
        return True
    else:
        return False


print(valid_polyndrome("A man, a plan, a canal: Panama"))
# print(valid_polyndrome("race a car"))
# print(valid_polyndrome(" "))
