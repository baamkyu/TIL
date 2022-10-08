T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                break

    # 공간 세팅
    visited = []
    queue = [start]
    result = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 미로 탐색
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            for k in range(4):
                ni = current[0] + di[k]
                nj = current[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0 and [ni, nj] not in visited:
                        queue.append([ni, nj])

                    if arr[ni][nj] == 3:
                        result = 1
                        break
    print(f'#{tc} {result}')