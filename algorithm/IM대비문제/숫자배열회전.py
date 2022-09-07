T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N*N 행렬
    data = [list(map(int, input().split())) for _ in range(N)]
    tmp_data_1 = []
    tmp_data_2 = []
    tmp_data_3 = []
    for i in range(N):              # 1열의 값
        for j in range(N-1, -1, -1):
            tmp_data_1.append(data[j][i])

    for i in range(N-1, -1, -1):    # 2열의 값
        for j in range(N-1, -1, -1):
            tmp_data_2.append(data[i][j])

    for i in range(N-1, -1, -1):    # 3열의 값
        for j in range(N):
            tmp_data_3.append(data[j][i])

    ans_lst = []
    for i in range(N):
        ans_lst.append(tmp_data_1[3*i:3*i+3])
        ans_lst.append(tmp_data_2[3*i:3*i+3])
        ans_lst.append(tmp_data_3[3*i:3*i+3])
    print(''.join(map(str, *ans_lst)))
