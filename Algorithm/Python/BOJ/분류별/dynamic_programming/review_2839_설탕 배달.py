import sys
input = sys.stdin.readline

N = int(input())

if N == 3:
    print(1)
elif N < 5:
    print(-1)
elif N == 5:
    print(1)
else:
    dp = [5001] * (N+1)
    dp[3] = dp[5] = 1
    for i in range(6, N+1):
        dp[i] = min(dp[i-3], dp[i-5]) + 1

    if dp[N] < 5001:
        print(dp[N])
    else:
        print(-1)