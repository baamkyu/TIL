import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    visit[idx] = 1
    for i in tree[idx]:
        if visit[i] == 0:
            cnt = dfs(i, cnt+1)
    return cnt

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    visit = [0] * (N+1)

    print(dfs(1, 0))