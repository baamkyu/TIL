def dijkstra(N, X, adj, d):
    for i in range(N+1):
        d[i] = adj[X][i]
    U = [X]
    for _ in range(N-1):    # N개의 정점 중 출발을 제외한 정점 선택
        w = 0
        for i in range(1, N+1):
            if (i not in U) and d[i] < d[w]:    # 남은 노드 중 비용이 최소인 w
                w = i
        U.append(w)
        for v in range(1, N+1):         # 정점 i가
            if 0 < adj[w][i] < 100000:  # w에 인접이면
                d[v] = min(d[v], d[w] + adj[w][v])  # i->v, i->w + w->v 값 비교

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    adj1 = [[100000]*(N+1) for _ in range(N+1)]     # 인접행렬 만들 준비
    for i in range(N+1):
        adj1[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c  # x->y의 비용은 c

    dout = [0] * (N+1)  # d out (나가는 방향)

    dijkstra(N, X, adj1, dout)
    print(dout)