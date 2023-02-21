def prim():
    dist = [100000]*(V+1)
    dist[V] = 0
    visited = [0] * (V+1)

    for _ in range(V+1):
        min_idx = None
        min_value = 100000

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]  # 최소값 갱신

        visited[min_idx] = 1    # 가장 작은 애로 이동할 거니까 visited 넣어주고
        print(visited, dist)

        # 이제 그 선택된 점에서부터 갈 수 있되, 더 짧은 거리를 보장한다면 dist 배열 갱신
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]
    return sum(dist)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접행렬 만들기
    adj = [[100000]*(V+1) for _ in range(V+1)]  # 가상으로 큰 수 넣어줌
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w
