T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [input() for _ in range(N)]
    cnt_lst = []    # 방향별 탐색의 결과들을 모아놓는 리스트

    # 가로 탐색
    cnt = 0
    for i in range(N):
        dol_cnt = 0
        for j in range(N):
            if data[i][j] == 'o':
                dol_cnt += 1
                if dol_cnt == 5:
                    cnt += 1
            if data[i][j] == '.':
                dol_cnt = 0

    cnt_lst.append(cnt)     # 가로 탐색 결과값을 cnt_lst에 추가해줌

    # 세로 탐색
    cnt = 0
    for i in range(N):
        dol_cnt = 0
        for j in range(N):
            if data[j][i] == 'o':
                dol_cnt += 1
                if dol_cnt == 5:
                    cnt += 1
            if data[j][i] == '.':
                dol_cnt = 0

    cnt_lst.append(cnt)     # 세로 탐색 결과값을 cnt_lst에 추가해줌

    # 대각선 오른쪽 탐색
    cnt = 0
    for i in range(N-5+1):
        dol_cnt = 0
        for j in range(N-5+1):
            for k in range(5):  # 오른쪽 방향 대각선
                if data[i+k][j+k] == 'o':
                    dol_cnt += 1
                    if dol_cnt == 5:
                        cnt += 1
                        break
                if data[i+k][j+k] == '.':
                    dol_cnt = 0

    cnt_lst.append(cnt)     # 오른쪽 방향 대각선 결과값을 cnt_lst에 추가해줌

    # 대각선 왼쪽 방향
    for i in range(N-5+1):
        dol_cnt = 0
        for j in range(4, N):
            for k in range(5):
                if data[i+k][j-k] == 'o':
                    dol_cnt += 1
                    if dol_cnt == 5:
                        cnt += 1
                        break
                if data[i+k][j-k] == '.':
                    dol_cnt = 0

    cnt_lst.append(cnt)

    print(f'#{tc}', end = ' ')
    if 1 in cnt_lst:
        print("YES")
    else:
        print("NO")