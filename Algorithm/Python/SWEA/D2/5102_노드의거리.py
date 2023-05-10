T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        