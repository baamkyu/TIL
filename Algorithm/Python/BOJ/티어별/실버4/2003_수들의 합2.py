# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
# 풀이
ans = 0
for i in prefix_sum:
    if i == M:
        ans += 1
    elif i > M:
        break
for i in range(1, N):
    for j in range(0, i+1):
      if prefix_sum[i] - prefix_sum[i-j] == M:
          ans += 1
print(ans)