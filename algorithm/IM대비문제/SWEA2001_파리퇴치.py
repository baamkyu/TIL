T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N*N 배열, M*M 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_hap = 0
    hap_lst = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            hap = 0
            for x in range(M):
                for y in range(M):
                    hap += arr[i+x][j+y]
                    hap_lst.append(hap)

    for i in range(len(hap_lst)):
        if max_hap < hap_lst[i]:
            max_hap = hap_lst[i]
    print(f'#{tc} {max_hap}')