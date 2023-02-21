'''
1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
'''

def find_set(x):
    if p[x] != x:   # x의 최종보스가 x가 아닌 경우
        p[x] = find_set(p[x])   # path compression
    return p[x]

def union(x, y):        # find_set(y) = p[y의 최종 보스]에 x의 최종 보스를 넣어라
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x:x[2])   # 가중치 기준 오름차순 정렬
    p = list(range(V+1))            # make_set

    ans = 0     # 가중치의 합
    cnt = 0     # 간선 선택 횟수

    for x, y, w in edges:
        if find_set(x) != find_set(y):   # 보스가 같지 않으면
            union(x, y)                 # 인수합병 시작
            ans += w                 # 가중치를 더해주고
            cnt += 1                    # 인수합병 횟수 카운트
        if cnt == V:
            break
    print(f'#{tc} {ans}')