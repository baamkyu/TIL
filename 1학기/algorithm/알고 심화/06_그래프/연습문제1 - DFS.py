def dfs(n):
    if n not in visited:
        visited.append(n)
    for i in range(len(arr)//2):
        if adj_matrix[n][i] and i not in visited: # n에서 갈 수 있는 곳이고, 방문한 적이 없다면
            dfs(i)

arr = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
adj_matrix = [[0]*8 for _ in range(len(arr)//2)]
for i in range(len(arr)//2):
    s = arr[i*2]
    e = arr[i*2+1]
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1
visited = []

dfs(1)
print(*visited)







# def dfs(n):
#     if n not in visited:
#         visited.append(n)
#     for destination in range(8):
#         if adj_matrix[n][destination] and destination not in visited:   # 갈 수 있는 방향이고 방문한 적이 없으면
#             dfs(destination)
#
# arr = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
# adj_matrix = [[0]*8 for _ in range(8)]
#
# # 갈 수 있는 방향을 행렬로 표현
# for i in range(len(arr)//2):
#     s = arr[i*2]
#     e = arr[i*2+1]
#     adj_matrix[s][e] = 1
#     adj_matrix[e][s] = 1
#
# stack = [1]
# visited = []
# dfs(1)
#
# print(visited)



