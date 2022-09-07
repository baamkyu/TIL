import sys
sys.stdin = open('SWEA1961_숫자배열회전.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    turn_90 = [[] for _ in range(N)]
    turn_180 = [[] for _ in range(N)]
    turn_270 = [[] for _ in range(N)]
    ans = [[] * N for _ in range(N)]
    cnt = 0
    for i in range(3):
        cnt += 1
        for x in range(N):
            for y in range(N-1, -1, -1):
                if cnt == 1:
                    turn_90[x].append(arr[y][x])
                    ans[x].append(arr[y][x])
                    continue
                elif cnt == 2:
                    turn_180[x].append(turn_90[y][x])
                    ans[x].append(turn_90[y][x])
                    continue
                elif cnt == 3:
                    turn_270[x].append(turn_180[y][x])
                    ans[x].append(turn_180[y][x])
                    continue
            ans[x].append('*')
    print(f'#{tc} ')
    for i in range(N):
        print(' '.join(''.join(map(str, ans[i])).split('*')))