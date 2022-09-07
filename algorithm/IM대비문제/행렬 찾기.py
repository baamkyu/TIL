T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    position = []
    cnt_i = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] >= 1:          # 0이 아닌 수부터 0일 때 까지 간 다음
                cnt_j = j
                while data[i][j] >= 1:   # i, j를 좌표에 찍는다.
                    cnt_j += 1
                print(cnt_j)

