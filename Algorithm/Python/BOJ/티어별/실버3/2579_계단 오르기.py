# 계단은 한번에 1개 혹은 2개 오를 수 있다.
# 연속된 3개의 계단을 모두 밟으면 안 된다.
# 마지막 도착 계단은 무조건 밟아야한다.
# 총 점수의 최대값을 구하여라.

import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * 301

for i in range(1, N+1):
    stairs[i] = int(input())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[N])