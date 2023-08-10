# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp = [0] * N
    dp[0] = 1
    dp[1] = 2
    for i in range(2, N):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007
    print(dp[-1])