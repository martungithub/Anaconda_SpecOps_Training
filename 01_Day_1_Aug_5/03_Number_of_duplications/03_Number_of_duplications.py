people = {'1': 10, '2': 20, '3': 15, '4': 25, '5': 65, '6': 20, '7': 15, '8': 25}

unique = {}
count = 0
for key, value in people.items():
    if value not in unique.values():
        unique[key] = value
count = len(people) - len(unique)

print("Number of duplications: ", count)
