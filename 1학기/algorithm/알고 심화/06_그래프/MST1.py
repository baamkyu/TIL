'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, v = map(int, input().split())
    adj_matrix[s][e] = v
    adj_matrix[e][s] = v
    adj_list[s].append((e, v))
    adj_list[e].append((s, v))
