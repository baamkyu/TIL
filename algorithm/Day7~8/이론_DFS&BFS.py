# stack 과 Queue의 차이점
# stack은 후입선출, Queue는 선입선출 (stack은 뒤에서부터 뽑을 것임, Queue는 앞에서부터 뽑을 것임)
# 장독대를 생각하자. stack은 위에서 뽑을 거고 Queue는 깨진 장독대라 아래에서 뽑을 거임


# 양방향 노드는 전치행렬이다. (이차원리스트로 표현했을 때)


# Tree는 포도알이 선의 개수보다 1개 더 많음

# DFS (Depth First Search, 깊이우선탐색)
# #input값
# 7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
# 1 2  # 다음 8개의 줄에 연결 정보를 제공
# 1 3
# 2 4
# 2 5  # 2번과 5번이 양방향으로 연결되어 있음!
# 4 6
# 5 6
# 6 7
# 3 7

V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1  # 양방향이기 때문에 두 줄 모두 써야함
    adj_matrix[end][start] = 1

stack = [1]
visited = []

while stack:  # stack이 빌 때까지 돌아라
    current = stack.pop()  # pop은 return값이 있어서 current에 들어감
    if current not in visited:  # visited안에 없으면 넣어라
        visted.append(current)

    for destination in range(V+1):
        if adj_matrix[current][destination] == 1 and destination not in visited:
            stack.append(destination)
print(adj_matrix)


#BFS (
V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

stack = [1]
visited = []























