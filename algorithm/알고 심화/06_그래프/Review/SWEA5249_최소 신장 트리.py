def union(x, y):
    p[find_set(y)] = find_set(x)

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key=lambda x:x[2])
    p = list(range(V+1))
    ans = 0
    cnt = 0

    for x, y, w in arr:
        if find_set(x) != find_set(y):
            union(x, y)
            ans += w
            cnt += 1        # 멈추는 조건을 걸어주기 위해
            if cnt == V:    # 싸이클이 돌면 break
                break
    print(f'#{tc} {ans}')