import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# 구간합
for _ in range(M):
    ans = 0
    i, j = map(int, input().split())
    ans = prefix_sum[j-1] - prefix_sum[i-1] + arr[i-1]
    print(ans)


# 시간 초과
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# for _ in range(M):
#     ans = 0
#     i, j = map(int, input().split())
#     for k in range(i-1, j):
#         ans += arr[k]
#     print(ans)