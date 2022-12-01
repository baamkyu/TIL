problem = 0
while True:
    problem += 1
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[100000]*N for _ in range(N)]
    dist[0][0] = arr[0][0]

    visited = []
    queue = [(0, 0)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while queue:
        min_rubee = 100000
        for q in queue:
            i = q[0]
            j = q[1]
            if (i, j) not in visited and dist[i][j] < min_rubee:
                min_rubee = dist[i][j]
                current = (i, j)
        visited.append(current)

        for k in range(4):
            ni = current[0] + di[k]
            nj = current[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in visited and arr[ni][nj] + dist[current[0]][current[1]] < dist[ni][nj]:
                    dist[ni][nj] = arr[ni][nj] + dist[current[0]][current[1]]
                    queue.append((ni, nj))
        if dist[N-1][N-1] != 100000:
            break

    print(f'Problem {problem}: {dist[N-1][N-1]}')

