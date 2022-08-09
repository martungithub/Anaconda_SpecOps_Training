def sorted_squares(data):
    data.sort()
    squares = []
    for i in data:
        squares.append(i * i)
    return squares


print(sorted_squares([1, 2, 3, 4, 0, 1, 2]))
