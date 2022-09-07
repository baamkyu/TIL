T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input)))) for _ in range(N)]
    visited = set()
    answer = 0

    initial_r = None
    initial_c = None
    for i in range(N):
        flag = False

        for j in range(N):
            if maze[i][j] == 2:
                initial_r = i
                initial_c = j
                flag = True
                break
        if flag:
            break