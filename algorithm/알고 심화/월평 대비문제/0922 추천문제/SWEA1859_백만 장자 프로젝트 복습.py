T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_arr = max(arr)
    ans = 0
    for i in range(N-1):
        if arr[i] <= max_arr:
            ans += max_arr - arr[i]
        if arr[i] == max_arr:
            max_arr = max(arr[i+1::])
    print(f'#{tc} {ans}')
