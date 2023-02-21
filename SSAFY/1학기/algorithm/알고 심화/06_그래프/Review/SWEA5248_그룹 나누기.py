'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''

def union(x, y):    # 자식의 p값은 조상의 p값을 따른다
    p[find_set(y)] = find_set(x)

def find_set(x):    # 인덱스와 x가 다르면 조상의 p값을 따른다
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 사람 수, M : 신청서 수
    arr = list(map(int, input().split()))
    p = list(range(N+1))    # make_set

    for i in range(M):      # x->y 선택, 둘의 부모가 다르면 같게 만들어줌
        x = arr[i*2]
        y = arr[i*2 + 1]
        if p[x] != p[y]:
            union(x, y)

    for i in range(N+1):    # 완전히 다 돌지 못했기 때문에 처음부터 다시 돌아줌
        find_set(i)

    print(f'#{tc} {len(set(p[1:]))}')