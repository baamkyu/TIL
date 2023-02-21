T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 이동 방향
    move_dict = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}

    # 블록을 만났을 때 바꿀 방향
    block_dict = {1: [1, 3, 0, 2], 2: [3, 0, 1, 2], 3: [2, 0, 3, 1], 4: [1, 2, 3, 0], 5: [1, 0, 3, 2]}

    max_score = 0

    for i in range(N):
        for j in range(N):
            # 핀볼 놓기
            if arr[i][j] == 0:
                start = [i, j]
                # 모든 방향으로 다 이동
                for move in move_dict:
                    score = 0
                    current = [i, j]
                    visited = set()
                    flag = False

                    while True:
                        # 현재 이동방향에 맞게 이동
                        current[0] += move_dict[move][0]
                        current[1] += move_dict[move][1]
                        # 이미 갔던 곳에서 같은 방향으로 이동하고 있다면 제외
                        if (current[0], current[1], move) not in visited:
                            visited.add((current[0], current[1], move))
                        else:
                            flag = True
                            break

                        # 벽과 만나면 점수 추가하고 이동 방향 변경
                        if current[0] == -1:
                            move = 1
                            score += 1
                        elif current[0] == N:
                            move = 0
                            score += 1
                        elif current[1] == -1:
                            move = 3
                            score += 1
                        elif current[1] == N:
                            move = 2
                            score += 1

                        # 블록과 만나면 점수 추가하고 해당 블록 모양에 맞게 변경
                        elif 0 < arr[current[0]][current[1]] <= 5:
                            score += 1
                            move = block_dict[arr[current[0]][current[1]]][move]

                        # 웜홀을 만나면
                        elif 6 <= arr[current[0]][current[1]] <= 10:
                            for p in range(N):
                                for q in range(N):
                                    # 같은 숫자의 웜홀 찾기
                                    if arr[p][q] == arr[current[0]][current[1]] and (p, q) != (current[0], current[1]):
                                        next_i = p
                                        next_j = q
                            # 웜홀 쌍으로 이동
                            current = [next_i, next_j]

                        elif arr[current[0]][current[1]] == -1 or [current[0], current[1]] == start:
                            break

                    if not flag and score > max_score:
                        max_score = score

    print(f'#{tc} {score}')
