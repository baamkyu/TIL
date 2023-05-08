# 3에 도달했을 때, -1해서 cnt_list에 추가
# 아래로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면
# 위로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면
# 왼쪽으로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면
# 오른쪽으로 이동, 좌표가 방문기록에 없고 좌표가 범위에 맞고 벽이 아니라면
def maze_dis(si, sj, cnt):
    return


T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, T+1):
    N = int(input())    # N*N
    arr = [list(map(int, input())) for _ in range(N)]

