T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    if N == 3:
        for i in range(1, N):    # N = 4인 경우 1 - 2~4순열 - 1
            for j in range(1, N):
                if i != j:
                    ans.append(e[0][i] + e[i][j] + e[j][0])
        print(f'#{tc} {min(ans)}')

    if N == 4:
        for i in range(1, N):    # N = 4인 경우 1 - 2~4순열 - 1
            for j in range(1, N):
                if i != j:
                    for k in range(1, N):
                        if i != k and j != k:
                            ans.append(e[0][i] + e[i][j] + e[j][k] + e[k][0])
        print(f'#{tc} {min(ans)}')