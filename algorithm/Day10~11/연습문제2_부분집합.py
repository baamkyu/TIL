arr = [1,2,3,4,5,6,7,8,9,10]
hap = 10
# 조합 2개뽑기 (그냥 조합)

for i in range(3):
    for j in range(i + 1, 3):  # i가 A일 때, j에 A는 제외하고 들어갈 수 있음.
        print(arr[i], arr[j])  # A B , A C , B C 3개 나옴.



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