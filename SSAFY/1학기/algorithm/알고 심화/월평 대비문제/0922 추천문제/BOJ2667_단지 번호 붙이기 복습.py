N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and (i,j) not in visited:
            cnt = 0
            stack = [(i, j)]

            while stack:
                current = stack.pop()
                if current not in visited:
                    cnt += 1

                    for k in range(4):
                        ni = current[0] + di[k]
                        nj = current[1] + dj[k]
                        if 0<=ni<N and 0<=nj<N:
                            if (ni, nj) not in visited and arr[ni][nj] == 1:
                                stack.append((ni, nj))
            home_list.append(cnt)
home_list.sort()
print(len(home_list))
for home in home_list:
    print(home)