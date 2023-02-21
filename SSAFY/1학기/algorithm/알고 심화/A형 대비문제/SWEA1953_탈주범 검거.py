T = int(input())
for tc in range(1, T+1):
    N, M, R, C, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [[], [1, -1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1,0]]
    dj = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]

    queue = [[R, C, 1]]    # 큐 생성
    visited = []    # 방문 기록
    cnt = 0         # 이동할 수 있는 장소 개수 저장할 변수

    while queue:
        current = queue.pop(0)
        if current[2] > time:    # 이동할 수 있는 시간을 넘으면, continue
            continue

        # 방문하지 않은 곳이면, 방문 기록 남기고 cnt + 1
        if [current[0], current[1]] not in visited:
            visited.append([current[0], current[1]])
            cnt += 1

            move = arr[current[0]][current[1]]  # current 좌표의 구조물 확인
            for k in range(len(di[move])):      # 구조물에 해당하는 방향으로 이동
                ni = current[0] + di[move][k]
                nj = current[1] + dj[move][k]

                if 0 <= ni < N and 0 <= nj < M:  # 터널을 벗어나지 않았으면
                    if [ni, nj] not in visited and arr[ni][nj]:
                        # 이동할 수 있는지 확인
                        if current[0] < ni: # 이동할 곳이 아래에 있는 경우
                            if arr[ni][nj] == 3 or arr[ni][nj] == 5 or arr[ni][nj] == 6:    # 아래로 가지 못하는 구조물(상 방향 없는 구조물)은 continue
                                continue
                        elif current[0] > ni: # 이동할 곳이 위에 있는 경우
                            if arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 7:    # 위로 가지 못하는 구조물(하 방향 없는 구조물)은 continue
                                continue
                        elif current[1] < nj: # 이동할 곳이 오른쪽에 있는 경우
                            if arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 5:    # 오른쪽으로 가지 못하는 구조물 (좌방향 없는 구조물)은 continue
                                continue
                        elif current[1] > nj: # 이동할 곳이 왼쪽에 있는 경우
                            if arr[ni][nj] == 2 or arr[ni][nj] == 6 or arr[ni][nj] == 7:    # 왼쪽으로 가지 못하는 구조물 (우방향 없는 구조물)은 continue
                                continue
                        queue.append([ni, nj, current[2]+1])

    print(f'#{tc} {cnt}')