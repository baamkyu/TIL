'''
상하좌우로 이동할 수 있음
이동하려는 방이 현재 방보다 1 커야함
근데 테스트케이스 이해가 안 된다
'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    max_list = []

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            start = [i, j]
            stack = [start]
            cnt = 1

            while stack:
                current = stack.pop()
                for k in range(4):
                    ni = current[0] + di[k]
                    nj = current[1] + dj[k]

                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] - arr[current[0]][current[1]] == 1:
                            stack.append([ni, nj])
                            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
                max_list = [arr[i][j]]
            elif cnt == max_cnt:
                max_list.append(arr[i][j])

    print(f'#{tc} {min(max_list)} {max_cnt}')