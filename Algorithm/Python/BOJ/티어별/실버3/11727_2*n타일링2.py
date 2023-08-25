# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[n]%10007)