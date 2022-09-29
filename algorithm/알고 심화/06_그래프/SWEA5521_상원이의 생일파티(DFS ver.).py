'''
2
6 5
2 3
3 4
4 5
5 6
2 5
6 5
1 2
1 3
3 4
2 3
4 5
'''
def dfs(i, N, c):
    if c == 3:  # 친구의 친구의 친구까지는 X
        return
    else:
        visited[i] = 1
        for j in range(1, N+1):
            if adjMatrix[i][j] and visited[j] == 0: # 친구이고 아직까지 초대장을 받지 않았으면
                dfs(j, N, c+1)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjMatrix = [[0] * (N+1) for _ in range(N+1)]   # 1~N번
    for _ in range(M):
        a, b = map(int, input().split())
        adjMatrix[a][b] = 1
        adjMatrix[b][a] = 1
    visited = [0] * (N+1)
    dfs(1, N, 0)
    print(f'#{tc} {sum(visited)}')

# 왜 안 되지? 디버깅 시도해보자!