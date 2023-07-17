# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 누적합
prefix_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(ans)



# 시간초과
# N, M = map(int, input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input().split())))

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     ans = 0
#     for x in range(x1-1, x2):
#         for y in range(y1-1, y2):
#             ans += arr[x][y]
#     print(ans)