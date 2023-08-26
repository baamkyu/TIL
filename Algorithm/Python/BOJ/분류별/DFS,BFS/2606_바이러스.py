# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
import sys
input = sys.stdin.readline

n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)