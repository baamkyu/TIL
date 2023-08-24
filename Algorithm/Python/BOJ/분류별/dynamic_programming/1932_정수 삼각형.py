import sys
input = sys.stdin.readline

N = int(input())
dp = []
for _ in range(N):
    tri = list(map(int, input().split()))
    dp.append(tri)

for i in range(1, N):
    for j in range(len(dp[i])):
        if j == 0:                # 맨 앞끼리 더하기
            dp[i][0] += dp[i-1][0]
        elif j == len(dp[i]) - 1: # 마지막 열끼리 더하기
            dp[i][-1] += dp[i-1][-1]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]
print(max(dp[N-1]))

# print(dp)

# 7
# 3 8
# 8 1 8
# 2 7 4 4
# 4 5 2 6 5

# dp[0][0]
# dp[0][0] + dp[1][0]   dp[0][0] + dp[1][1]
# dp[1][0] + dp[2][0]   max(dp[1][0], dp[1][1]) + dp[2][1]   dp[1][1] + dp[2][2]
# dp[2][0] + dp[3][0]   max(dp[2][0], dp[2][1]) + dp[3][1]   max(dp[2][1], dp[2][2]) + dp[3][2]