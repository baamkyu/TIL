import sys
input = sys.stdin.readline


def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M): 
            if matrix[nx][ny] == 1:
              # 방문했다는 표시 -1
              matrix[nx][ny] = -1
              dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())   # M: 가로길이, N: 세로길이, K: 배추 개수
    matrix = [[0]*M for _ in range(N)]
    ans = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)