import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weight = [0] + list(map(int, input().split()))

groups = [list(map(int, input().split())) for _ in range(M)]

check = [1] * (N+1)
check[0] = 0

for g in groups:
    if weight[g[0]] < weight[g[1]]:
        check[g[0]] = 0
    elif weight[g[0]] > weight[g[1]]:
        check[g[1]] = 0
    else:
        check[g[0]] = 0
        check[g[1]] = 0
print(check.count(1))