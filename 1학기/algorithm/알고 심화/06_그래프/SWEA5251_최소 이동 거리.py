def dijkstra():
    dist = [10000]*(V+1)
    dist[0] = 0  # 자기자신한테 가는 거리는 0
    visited = [0]*(V+1)  # 방문했던 곳 표시

    for _ in range(V+1):
        min_idx = 0
        min_value = 10000

        for i in range(V+1):     # 일단 현재 dist배열에서 visited안 된 애들 중 가장 작은 로직 찾는 로직
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True  # 가장 작은 애로 이동

        for i in range(V+1):
            if not visited[i] and dist[i] > adj_matrix[min_idx][i] + dist[min_idx]:  # 방문한 적이 없고
                dist[i] = adj_matrix[min_idx][i] + dist[min_idx]
    return dist[V]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    adj_matrix = [[987654321]*(V+1) for _ in range(V+1)]     # 인접행렬

    for i in range(E):          # 인접행렬 만들기
        s, e, w = map(int, input().split())
        adj_matrix[s][e] = w    # 노드들간의 가중치 자체를 인접 행렬에 넣어서 구조화

    print(f'#{tc} {dijkstra()}')

