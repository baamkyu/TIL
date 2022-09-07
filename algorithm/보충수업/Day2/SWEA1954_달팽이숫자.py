import sys
sys.stdin = open('SWEA1954_달팽이숫자.txt')

T = int(input())

di = [0, 1, 0, -1]  # 우 하 좌 상
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = 0
    j = 0
    dr = 0

    for cnt in range(1, N*N+1):
        arr[i][j] = cnt

        ni, nj = i+di[dr], j+dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
            i, j, = ni, nj
        else:   # 범위를 벗어나거나 범위에 값이 있는 경우
            dr = (dr+1)%4
            i, j = i + di[dr], j + dj[dr]
    print(f'#{tc}')
    for lst in arr:
        print(*lst)