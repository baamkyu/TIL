T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    min_num = 999999999
    max_num = 0
    for i in range(n):
        if arr[i] < min_num:
            min_num = arr[i]
        elif arr[i] > max_num:
            max_num = arr[i]
    print(f'#{tc} {max_num - min_num}')