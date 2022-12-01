T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    arr2 = [[0] * max(arr) for _ in range(N)]
    for i in range(max(arr)):
        for j in range(N):
             arr2[i][j] = arr[j][i]
    print(arr2)
    3