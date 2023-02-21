def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    p = list(range(V+1))            # make_set
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x:x[2])   # 가중치 기준으로 정렬

    ans = 0
    cnt = 0

    for i in range(len(edges)):
        x = edges[i][0]
        y = edges[i][1]
        if find_set(x) != find_set(y):  # 조상이 같지 않으면 연결해도 상관X
            union(x, y)
            cnt += 1
            ans += edges[i][2]
            if cnt == V:        # 간선 수만큼 (?)
                break

    print(f'#{tc} {ans}')