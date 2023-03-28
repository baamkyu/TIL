T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    
    num = 0 # 0부터 시작
    r = -1  # 첫번째에 오른쪽으로 이동하므로 -1부터 시작
    c = 0   # column = 0에서 시작

    # 우 - 하 - 좌 - 상 방향
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    turn = 0
    
    for i in range(2*N, 1, -1):
        for _ in range(i//2):
            num += 1
            r = r + dr[turn % 4]
            c = c + dc[turn % 4]
            snail[c][r] = num
        turn += 1

    # 답안 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()

    # 답안 출력 방법2
    # print(f'#{tc}')
    # for i in range(N):
    #   print(*snail[i])
