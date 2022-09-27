N = 10
for tc in range(1, N+1):
    testcase = int(input())
    arr = [list(map(int,input())) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]

    # 출발 점 찾기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                start = [[i,j]]
            elif arr[i][j] == 3:
                end_i, end_j = i, j

    while start:
        start_i, start_j = start.pop()

        # 왔던 곳이면 넘어가기
        if not visited[start_i][start_j]:
            visited[start_i][start_j] = 1

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            if 0 <= start_i + di[k] < 100 and 0 <= start_j + dj[k] < 100:
                if visited[start_i + di[k]][start_j + dj[k]] == 0:
                    if arr[start_i + di[k]][start_j + dj[k]] == 0 or arr[start_i + di[k]][start_j + dj[k]] == 3:
                        start.append([start_i + di[k], start_j + dj[k]]

    if visited[end_i][end_j]:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))