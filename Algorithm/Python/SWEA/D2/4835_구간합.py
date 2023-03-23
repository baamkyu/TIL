T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    min_sum = 9999999 # 임시 최소값
    max_sum = 0       # 임시 최대값
    for i in range(N-M+1):
        num_sum = 0
        for j in range(M):
            num_sum += arr[i+j]
        if num_sum < min_sum:
            min_sum = num_sum
        if max_sum < num_sum:
            max_sum = num_sum
    print(f'#{tc} {max_sum - min_sum}')
            
    