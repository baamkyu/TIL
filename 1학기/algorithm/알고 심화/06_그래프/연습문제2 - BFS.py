def bfs(n):


arr = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
adj_matrix = [[0]*8 for _ in range(len(arr)//2)]

for i in range(len(arr)//2):
    s, e = arr[i*2], arr[i*2+1]
    adj_matrix[s][e] = 1
    adj_matrix[e][s] = 1
