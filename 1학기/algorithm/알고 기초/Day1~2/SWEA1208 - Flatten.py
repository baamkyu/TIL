import sys
sys.stdin = open('SWEA1208 - Flatten.txt', 'r')

T = 10
for tc in range(1, T+1):
    max_dump = int(input())
    y = list(map(int, input().split()))
    for i in range(max_dump):
        y.sort()
        y[0] += 1
        y[-1] -= 1
    max_minus_min = max(y)-min(y)
    print(f'#{tc} {max_minus_min}')