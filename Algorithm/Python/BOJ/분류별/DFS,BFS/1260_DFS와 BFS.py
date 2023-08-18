# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
import sys
input = sys.stdin.readline

from collections import deque

def dfs(v):
  dfs_visit_list[v] = 1        
  print(v, end = " ")
  for i in range(1, N + 1):
    if dfs_visit_list[i] == 0 and graph[v][i] == 1:
      dfs(i)

def bfs(v):
  q = deque()
  q.append(v)       
  bfs_visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, N + 1):
      if bfs_visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        bfs_visit_list[i] = 1


N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 탐색 시작할 정점의 번호
graph = [[0] * (N+1) for _ in range(N+1)]
dfs_visit_list = [0] * (N+1)
bfs_visit_list = [0] * (N+1)


# 간선 표시
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = 1
# print(graph)

# q = deque()
dfs(V)
print()
bfs(V)