def strmove(data, move):
    data = data[len(data) - move:] + data[:len(data) - move]
    return data


print(strmove("hello", 2))
