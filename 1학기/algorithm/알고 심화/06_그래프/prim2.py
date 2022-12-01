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

def prim2(r, V):
    MST = [0] * (V+1)   # MST 포함 여부
    MST[r] = 1          # 시작 정점 표시
    hap = 0             # MST 간선의 가중치 합

    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[v] == 0), key가 최고인 u 찾기
        s = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):    # MST에 포함된 정점i와 인접한 정점j중 MST에 포함(?)
                    if adj_matrix[i][j] > 0 and MST[j] == 0 and minV > adj_matrix[i][j]:
                        s = j
                        minV = adj_matrix[i][j]
        hap += minV
        MST[s] = 1
    return hap

V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, value = map(int, input().split())
    adj_matrix[s][e] = value
    adj_matrix[e][s] = value
print(prim2(0, V))