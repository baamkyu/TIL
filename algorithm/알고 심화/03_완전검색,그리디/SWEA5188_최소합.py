'''
1
3
1 2 3
2 3 4
3 4 5
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)



    for i in range(1, N):   # 첫번째 열, 행은 합으로 다 더해놓고 시작
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]

    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + arr[i][j]

    print(f'#{tc} {arr[N-1][N-1]}')
