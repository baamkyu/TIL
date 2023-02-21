T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    N_lst = list(map(int, input().split()))
    M_lst = list(map(int, input(). split()))
    hap_lst = []
    if N < M:       # M이 더 긴 숫자열일 때
        for j in range(M-N+1):
            hap = 0
            for i in range(N):
                hap += M_lst[j+i] * N_lst[i]
            hap_lst.append(hap)
    if N > M:       # N이 더 긴 숫자열일 때
        for j in range(N-M+1):
            hap = 0
            for i in range(M):
                hap += N_lst[j+i] * M_lst[i]
            hap_lst.append(hap)
    max_hap_lst = max(hap_lst)
    print(f'#{tc} {max_hap_lst}')