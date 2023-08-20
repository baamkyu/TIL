# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
import sys
input = sys.stdin.readline

from collections import deque

def dfs(v):
  dfs_visit_list[v] = 1        
  print(v, end = " ")
  # 재귀함수 선언 (v와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
  for i in range(1, N + 1):
    if dfs_visit_list[i] == 0 and graph[v][i] == 1:
      dfs(i)

def bfs(v):
  q = deque()
  q.append(v)   # 방문해야할 곳을 순서대로 넣음       
  bfs_visit_list[v] = 1   # 방문 체크
  while q:      # 큐 안에 데이터가 없을 때까지
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, N + 1):
      if bfs_visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        bfs_visit_list[i] = 1


N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 탐색 시작할 정점의 번호
graph = [[0] * (N+1) for _ in range(N+1)] # 인접행렬 생성
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