import sys
sys.stdin = open('SWEA1979_어디에 단어가 들어갈 수 있을까.txt', 'r')

    T = int(input())
    for tc in range(1, T+1):
        N, K = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]
        cnt = 0

        for i in range(N):
            arr_cnt = 0
            for j in range(N):
                if arr[i][j] == 1:
                    arr_cnt += 1
                    if arr_cnt == K:
                        cnt += 1
                    if arr_cnt == K+1:
                        cnt -= 1
                if arr[i][j] == 0:
                    arr_cnt = 0

        for i in range(N):
            arr_cnt = 0
            for j in range(N):
                if arr[j][i] == 1:
                    arr_cnt += 1
                    if arr_cnt == K:
                        cnt += 1
                    if arr_cnt == K+1:
                        cnt -= 1
                if arr[j][i] == 0:
                    arr_cnt = 0
        print(f'#{tc} {cnt}')


