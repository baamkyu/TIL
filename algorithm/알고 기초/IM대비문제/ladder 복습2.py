T = 10
for tc in range(1, T+1):
    N = int(input())    # 덤프 횟수
    data = list(map(int, input().split()))  # 테스트케이스
    while N > 0:
        data.sort()
        data[0] += 1
        data[-1] -= 1
        N -= 1
    print(f'#{tc}', end = ' ')
    print(max(data) - min(data))