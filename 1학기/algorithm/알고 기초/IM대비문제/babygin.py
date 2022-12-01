T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input()))
    cnt = 0     # 2이면 babygin이다.

    data_arr = [0] * 10
    for i in data:
        data_arr[i] += 1

    for i in range(len(data_arr)-2):
        if data_arr[i] == 6:    # 한 가지 수가 6개 있으면 cnt = 2
            cnt = 2
        if data_arr[i] == data_arr[i+1] == data_arr[i+2] == 2:  # 연속된 3개의 수가 2개씩 있으면 cnt = 2
            cnt = 2

        if data_arr[i] == 3:    # 한 가지 수가 3개 있으면 cnt += 1
            cnt += 1
        if data_arr[i] == data_arr[i+1] == data_arr[i+2] == 1:  # 연속된 3개의 수가 1개씩 있으면 cnt = 1
            cnt += 1

    for i in range(len(data_arr)-5):    # 6개 연속된 수는 범위가 달라서 for문을 따로 빼줘야함
        if data_arr[i] == data_arr[i+1] == data_arr[i+2] == data_arr[i+3] == data_arr[i+4] == data_arr[i+5] == 1:   # 연속된 6개의 수가 있으면 cnt = 2
            cnt = 2

    print(f'#{tc} ', end = '')
    if cnt == 2:
        print(1)    # babygin
    else:
        print(0)    # babygin이 아님