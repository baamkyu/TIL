# 운영 비용 = K * K + (K - 1) * (K - 1)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
