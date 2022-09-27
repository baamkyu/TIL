T = 10
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    buildings = list(map(int, input().split()))
    for i in range(2, N-2):
        if buildings[i] >= buildings[i-1] and buildings[i] >= buildings[i-2] and buildings[i] >= buildings[i+1] and buildings[i] >= buildings[i+2]:
            cnt += buildings[i] - max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
    print(f'#{tc} {cnt}')