T = int(input()) # 테스트케이스의 수
for tc in range(T):
    N = int(input())  # N * N 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0] # ni가 움직일 방향
    dj = [0, 1, 0, -1] # nj가 움직일 방향

    all_list = []
    for i in range(N):
        for j in range(N):
            tmp_arr = []
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    tmp_arr = abs(arr[ni][nj] - arr[i][j])  # i, j 기준으로 상 우 하 좌 (시계방향)
            all_list += [tmp_arr]
    hap = 0
    for a in all_list:
        hap += a
    print(hap)


            #     if ni<0 or ni>=N or nj<0 or nj>=N:
            #         continue
            # answer+= abs(arr[i][j] + arr[nr][nc])
    # sum_list = []x
    # for a in range(len(all_list)):
    #     sum_list.append(sum(all_list[a]))
    # print(max(sum_list))