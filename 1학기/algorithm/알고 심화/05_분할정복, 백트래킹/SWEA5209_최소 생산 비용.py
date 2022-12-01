def minimum(depth, temp):
    global ans
    if depth == N:    # 마지막까지 갔을 때 ans에 temp값을 넣어줌
        if ans > temp:
            ans = temp

    if temp >= ans:     # 백트래킹
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            minimum(depth+1, temp+arr[depth][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1500
    visited = [0]*N

    minimum(0, 0)
    print(f'#{tc} {ans}')