def powerset(depth):
    global ans
    if depth == len(arr):
        subset = []
        for i in range(len(check)):
            if check[i]:
                subset.append(arr[i])
        if sum(subset) == 10:
            ans += 1
        return
    else:
        check[depth] = 0
        powerset(depth + 1)

        check[depth] = 1
        powerset(depth + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [0] * len(arr)
ans = 0
powerset(0)
print(ans)