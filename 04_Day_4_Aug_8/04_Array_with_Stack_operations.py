def buildArray(target, n):
    ans = []
    move = 0
    for i in range(1, n + 1):
        ans.append("Push")
        move += 1
        if i not in target:
            ans.append("Pop")
            move -= 1
        if move == len(target):
            break
    return ans


print(buildArray([1, 3], 3))
