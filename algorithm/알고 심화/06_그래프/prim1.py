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


def prim1(r, V):
    MST = [0] * (V+1)   # MST 포함 여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화
    key[r] = 0          # 시작 정점의 key
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중 (MST[v] == 0), key가 최고인 u 찾기
        s = 0
        minV = 10000
        for i in range(V+1):
            if MST[i] == 0 and key[i] < minV:
                s = i
                minV = key[i]
        MST[s] = 1  # 정점 u를 MST에 추가
        # s에 인접인 e에 대해, MST에 포함되지 않은 정점이면
        for e in range(V+1):
            if MST[e] == 0 and adj_matrix[s][e] > 0:
                key[e] = min(key[e], adj_matrix[s][e])  # s를 통해 MST에 포함되는 비용과 기존의 비용 비교
    print(key)
    return sum(key)     # MST 가중치의 합

V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, value = map(int, input().split())
    adj_matrix[s][e] = value
    adj_matrix[e][s] = value
print(prim1(0, V))




# 라이브 교수님이 작성한 코드
# def prim1(r, V):
#     MST = [0] * (V+1)    # MST 포함 여부
#     key = [10000]*(V+1)  # 가중치의 최대값 이상으로 초기화
#     key[r] = 0           # 시작정점의 key
#     for _ in range(V):   # v+1개의 정점 중 v개를 선택
#         # MST에 포함되지 않은 정점 중 (MST[u]==0), key가 최소인 u 찾기
#         u = 0
#         minV = 10000
#         for i in range(V+1):
#             if MST[i] == 0 and key[i] < minV:
#                 u = i
#                 minV = key[i]
#         MST[u] = 1      # 정점 u를 MST에 추가
#         # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
#         for v in range(V+1):
#             if MST[v] == 0 and adjM[u][v] > 0:
#                 key[v] = min(key[v], adjM[u][v])    # u를 통해 MST에 포함되는 비용과 기존의 비용을 비교
#     return sum(key)
#
# V, E = map(int, input().split())
# adjM = [[0]*(V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w
#     adjM[v][u] = w
# print(prim1(0, V))
