def find_set(x):
    while x != rep[x]:  # 자기 자신을 가리킬때까지
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, value = map(int, input().split())
    edge.append([s, e, value])
edge.sort(key=lambda x:x[2])        # 2번 인덱스(3번째) 원소인 value 기준으로 배열
rep = [i for i in range(V+1)]       # 대표원소 배열

# MST의 간선수 N = 정점 수 - 1
N = V + 1   # 실제 정점 수
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합
for s, e, value in edge:
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += value
        if cnt == N-1:  # 간선 수
            break
print(total)