r, c = map(int, input().split())

graph = [[0] * c for _ in range(r)]
copy = [[0] * c for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):

    j = 0
    for s in input():
        if s == "X":
            graph[i][j] = 1

        j += 1

for i in range(r):
    for j in range(c):
        copy[i][j] = graph[i][j]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:
            cnt = 0

            for n in range(4):
                ax = i + dx[n]
                ay = j + dy[n]

                if r <= ax or ax < 0 or c <= ay or ay < 0:
                    cnt += 1

                else:
                    if graph[ax][ay] == 0:
                        cnt += 1

            if cnt > 2:
                copy[i][j] = 0


# 출력
row = []
col = []

dic = {0: ".", 1: "X"}

for i in range(r):
    for j in range(c):
        if copy[i][j] == 1:
            row.append(i)
            col.append(j)

if row:
    row_l = min(row)
    row_h = max(row)
    col_l = min(col)
    col_h = max(col)

    for i in range(row_l, row_h + 1):
        for j in range(col_l, col_h + 1):
            print(dic[copy[i][j]], end="")
        print()

else:
    print('X')