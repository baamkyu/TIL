'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''

T = int(input())
for tc in range(1, T+1):
    # N : 화물 수, M : 트럭 수
    N, M = map(int, input().split())

    # N개의 화물 무게
    weights = sorted(list(map(int, input().split())), reverse=True)

    # M개 트럭의 최대 적재 무게
    max_weights = sorted(list(map(int, input().split())), reverse=True)

    now = [0] * M   # 트럭 현황

    for j in range(N):      # 컨테이너
        for i in range(M):  # 트럭
            if max_weights[i] >= weights[j]:
                if not now[i]:   # now[i]가 비어있으면
                    now[i] = weights[j]
                    break
    print(f'#{tc} {sum(now)}')
