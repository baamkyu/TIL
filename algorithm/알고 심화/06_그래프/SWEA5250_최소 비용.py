T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    costs = [[10000]*N for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    costs[0][0] = 0
    queue = []
    queue.append((0, 0))

    while queue:
        current = queue.pop(0)
        r, c = current  # 방문한 행, 열 번호
        for i in range(4):
            if 0 <= r + di[i] < N and 0 <= c + dj[j] < N:
                cost = 1
                if queue[r][c] < queue[r + di[i]][c + dj[j]]:
                    cost +=