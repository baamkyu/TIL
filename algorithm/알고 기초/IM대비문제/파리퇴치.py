T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hap_lst = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            hap = 0
            for k in range(M):
                for l in range(M):
                    hap += arr[i+k][j+l]
            hap_lst.append(hap)
    print(f'#{tc}', end = ' ')
    print(max(hap_lst))
