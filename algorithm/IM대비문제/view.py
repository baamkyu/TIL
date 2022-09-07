T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0     # 조망권 확보 건물 수
    for i in range(2, N-2):     # 앞 2개와 뒤 2개는 조망권 확보 불가능
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            # print(arr[i], arr[i-1], arr[i-2], arr[i+1], arr[i+2])
            cnt += arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
    print(f'#{tc} {cnt}')
