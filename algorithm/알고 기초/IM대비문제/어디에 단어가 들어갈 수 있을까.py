T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 가로로 입력 가능한 개수
    for i in range(N):
        arr_cnt = 0
        for j in range(N):
            if data[i][j] == 1:     # 1이면 arr_cnt += 1
                arr_cnt += 1
                if arr_cnt == K:    # arr_cnt가 K와 같아지면 cnt += 1
                    cnt += 1
                if arr_cnt > K:     # arr_cnt가 K보다 커지면 더한 cnt값 빼고 초기화
                    cnt -= 1
                    break
            if data[i][j] == 0:     # 값이 0이면 arr_cnt 초기화
                arr_cnt = 0

    # 세로로 입력 가능한 개수
    for i in range(N):
        arr_cnt = 0
        for j in range(N):
            if data[j][i] == 1:     # 1이면 arr_cnt += 1
                arr_cnt += 1
                if arr_cnt == K:    # arr_cnt가 K와 같아지면 cnt += 1
                    cnt += 1
                if arr_cnt > K:     # arr_cnt가 K보다 커지면 더한 cnt값 빼고 초기화
                    cnt -= 1
                    break
            if data[j][i] == 0:     # 값이 0이면 arr_cnt 초기화
                arr_cnt = 0

    print(cnt)