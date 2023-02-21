'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

def root_sum(i, j, cnt):
    global min_cnt
    if i == N or j == N:
        return

    cnt += arr[i][j]

    if i == N-1 and j == N-1:
        if cnt < min_cnt:
            min_cnt = cnt

    if cnt > min_cnt:   # 백트래킹
        return

    for di, dj in [[1,0], [0,1]]:
        root_sum(i+di, j+dj, cnt)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cnt = 1000000
    root_sum(0, 0, 0)
    print(f'#{tc} {min_cnt}')



# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(1, N):   # 첫번째 열, 행은 합으로 다 더해놓고 시작
#         arr[0][i] += arr[0][i-1]
#         arr[i][0] += arr[i-1][0]
#
#     for i in range(1, N):
#         for j in range(1, N):
#             arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + arr[i][j]
#
#     print(f'#{tc} {arr[N-1][N-1]}')
