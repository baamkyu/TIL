T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(N)]

    # 가로
    for i in range(N):
        arr_cnt = 0
        for j in range(N):
            if data[i][j] == 1:
                arr_cnt += 1
                if arr_cnt == K:
                    cnt += 1
                if arr_cnt > K:
                    cnt -= 1
                    break
            if data[i][j] == 0:
                arr_cnt = 0
    # 세로
    for i in range(N):
        arr_cnt = 0
        for j in range(N):
            if data[j][i] == 1:
                arr_cnt += 1
                if arr_cnt == K:
                    cnt += 1
                if arr_cnt > K:
                    cnt -= 1
                    break
            if data[j][i] == 0:
                arr_cnt = 0
