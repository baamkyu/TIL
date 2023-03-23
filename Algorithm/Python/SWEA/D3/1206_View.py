T = 10
for tc in range(1, T+1):
    n = int(input())
    answer = 0
    arr = list(map(int,input().split()))
    for i in range(2, n-2):
        if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
            answer += (arr[i] - max(arr[i-2], arr[i-1], arr[i+1], arr[i+2]))
    print(f'#{tc} {answer}')