def find_set(x):
    if p[x] != x:   # p[x]와 x가 다르면 p[x] = 조상
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):    # 자식의 p값은 조상의 p값을 따른다
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N:사람 수, M:쌍 수
    arr = list(map(int, input().split()))
    p = list(range(N+1))    # make_set

    for i in range(M):
        x = arr[i*2]
        y = arr[i*2 + 1]
        if p[x] != p[y]:    # 조상의 p값과 자식의 p값이 다르면 union(x,y)
            union(x,y)

    for i in range(N+1):    # p값을 한 번 더 돌아줌
        find_set(i)

    print(f'#{tc} {len(set(p[1:]))}')  # p[0]값은 0이 들어가므로 1부터 출력

