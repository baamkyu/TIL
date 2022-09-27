def change(depth, battery, cnt):
    global min_cnt
    if depth == N-1:    # 목적지까지 도달했을 때
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if battery > 0:
        change(depth+1, battery-1, cnt)

    if cnt < min_cnt - 1:
        change(depth+1, arr[depth]-1, cnt+1)


T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    arr = temp[1:]
    min_cnt = N

    change(0, 0, -1)
    print(f'#{tc} {min_cnt}')