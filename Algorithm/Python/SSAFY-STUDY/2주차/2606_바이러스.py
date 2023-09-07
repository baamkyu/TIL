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
graph = [[] for _ in range(n+1)]  # n+1개의 빈 리스트 생성
# print(graph)
visited = [0] * (n+1)

for i in range(v):
    a,b = map(int,input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향

# 1 2, 1 3 으로 인풋을 주어지면 graph = [[2, 3], [1], [1]]
# print(graph)

def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)  # 1번에서 출발
print(sum(visited)-1) # 1번을 제외한 감염된 컴퓨터 수

