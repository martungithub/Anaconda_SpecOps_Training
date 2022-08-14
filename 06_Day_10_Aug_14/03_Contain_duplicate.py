def contain_dupblicate(data):
    for i in data:
        if data.count(i) > 1:
            return True
        return False


print(contain_dupblicate([1, 2, 3, 4, 1]))
