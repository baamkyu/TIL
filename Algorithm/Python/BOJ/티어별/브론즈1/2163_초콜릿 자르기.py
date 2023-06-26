# 정화는 N×M 크기의 초콜릿을 하나 가지고 있다.
# 초콜릿의 크기가 주어졌을 때, 이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하라.
N, M = map(int, input().split())
if N == 1 and M == 1:
    ans = 0
elif N == 1 and M == 2 or N == 1 and M == 1:
    ans = 1
else:
    ans = N * M - 1

print(ans)