import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
# n = 4인 경우, x[0](x[1]+x[2]+x[3]) + x[1](x[2]+x[3]) + x[2](x[3])

# 구간합
prefix_sum = [0] * n
prefix_sum[0] = nums[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

# x[2] + x[3] = prefix_sum[3] - prefix_sum[1]
ans = 0
for i in range(1, n):
    ans += nums[i-1] * (prefix_sum[n-1] - prefix_sum[i-1])
print(ans)