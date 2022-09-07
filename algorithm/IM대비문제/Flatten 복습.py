T = 10
for tc in range(1, T+1):
    dump = int(input())
    data = list(map(int, input().split()))
    sort_data = data    # 기본 값
    while dump > 0:
        sort_data = sorted(sort_data)
        sort_data[-1] -= 1
        sort_data[0] += 1
        dump -= 1
    print(f'#{tc}', end = ' ')
    print(max(sort_data) - min(sort_data))
