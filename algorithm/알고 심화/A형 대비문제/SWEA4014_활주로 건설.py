T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 경사로의 길이 X는 2이상 4이하의 정수

    # 가로 탐색
    for k in range(N):
        board = arr[k]
        pre = board[0]
        i = 1
        while i < N:
            if pre == board[i]:     # 같은 값이 연속되면 + 1
                cnt += 1
            else:
                if pre + 1 == board[i]: # 오르막
                    if cnt < X:
                        break
                    elif cnt >= X:
                        cnt = 1
                        pre += 1
                elif pre - 1 == board[i]:   # 내리막
                    for j in range(N-i):
                        if
                    if cnt < X:

                else:
                    break