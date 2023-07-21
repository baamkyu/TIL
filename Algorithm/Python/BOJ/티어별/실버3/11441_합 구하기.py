# 첫째 줄에 수의 개수 N이 주어진다
# 그 아래 M개의 줄에는 각 구간을 나타내는 i와 j가 주어진다.
# 총 M개의 줄에 걸쳐 입력으로 주어진 구간의 합을 출력한다.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 누적합
prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# 풀이
M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    ans = prefix_sum[end - 1] - prefix_sum[start-1] + arr[start-1]
    print(ans)