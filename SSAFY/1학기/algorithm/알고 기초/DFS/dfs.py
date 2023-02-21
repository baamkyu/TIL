'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

# 스택 + 인접 행렬
V, E = map(int, input().split())
adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1  # 양방향 !!
    adj_matrix[end][start] = 1

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if adj_matrix[current][destination] and destination not in visited:
            stack.append(destination)
print('이동경로 :', *visited)


# 재귀 + 인접행렬
def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)

V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = []
dfs(1)

print('이동경로 :', *visited)