for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = [i, j]

    visited = []
    queue = [start]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    result = 0

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)

            for k in range(4):
                ni = current[0] + di[k]
                nj = current[1] + dj[k]

                if arr[ni][nj] == 0 and [ni, nj] not in visited:
                    queue.append([ni, nj])

                if arr[ni][nj] == 3:
                    result = 1
                    break
    print(f'#{tc} {result}')