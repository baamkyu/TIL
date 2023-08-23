import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

# 1 1 1 2 2 3 4 5 7 9 12
# 1         0번
# 1         1번
# 1         2번
# 1+1 = 2   3번   # 
# 1+1 = 2   4번   # 
# 2+1 = 3   5번   # 4번+0번
# 3+1 = 4   6번   # 5번+1번
# 4+1 = 5   7번   # 6+2
# 5+2 = 7   8번   # 7+3
# 7+2 = 9   9번   # 8+4
# 9+3 = 12  10변  # 9+5


for i in range(5, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(input())
    print(dp[N])