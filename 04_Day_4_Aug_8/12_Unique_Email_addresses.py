def first(arr, x):
    low = 0
    high = len(arr)
    res = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1

    return res


def last(arr, x):
    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1

        else:
            res = mid
            low = mid + 1

    return res


answer = []
arr = [5, 7, 7, 8, 8, 10]
target = 8

answer.append(first(arr, target))
answer.append(last(arr, target))

print(answer)
