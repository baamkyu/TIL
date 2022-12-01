T = 10
for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    now_i = 0
    now_j = 0
    for i in range(100):
        for j in range(100):
            if data[i][j] == 2:
                now_i = i
                now_j = 98
            # 시작점 : data[now_i][98], 이유 - 도착지점의 j는 99이고 그 위는 무조건 1이기 때문
                while now_j > 0:
                    if now_i > 0 and data[now_i-1][now_j] == 1:       # 시작점의 왼쪽이 1이면 왼쪽으로 이동
                        now_i -= 1
                    elif now_i < 99 and data[now_i+1][now_j] == 1:     # 좌표의 오른쪽이 1이면 오른쪽으로 이동
                        now_i += 1
                    else:                               # 왼쪽 오른쪽이 둘 다 0이면 위로 이동
                        now_j -= 1
                break
            print(now_i)
            print(now_j)

    # for j in range(10):
    #     for i in range(10):
    #         if data[i][0] == 1:
    #             now_i = i
    #             now_j = 0
    #             if now_i > 0 and data[now_i][now_j-1] == 1:       # 왼쪽에 1이 있을 때
    #                 now_j -= 1                 # J좌표는 왼쪽으로 간다 (i좌표 그대로)
    #             elif now_i < 9 and data[now_i][now_j+1] == 1:     # 오른쪽에 1이 있을 때
    #                 now_j += 1                 # J좌표는 오른쪽으로 간다 (i좌표 그대로)
    #             else:
    #                 now_i += 1               # 아닌 경우에는 i좌표가 아래로 간다
    #             if now_j == 9:
    #                 print(now_i)
    #         else:
    #             pass