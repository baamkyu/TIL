import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rule_speed = [0]*101

now_n = 1
for _ in range(N):
    rng, spd = map(int, input().split())
    for i in range(now_n, rng + now_n):
        rule_speed[i] = spd
    now_n = rng + now_n

test_speed = [0] * 101
now_m = 1
for _ in range(M):
    rng, spd = map(int, input().split())
    for i in range(now_m, rng + now_m):
        test_speed[i] = spd
    now_m = rng + now_m

ans = 0
for i in range(1, 101):
    if test_speed[i] - rule_speed[i] > ans:
        ans = test_speed[i] - rule_speed[i]
print(ans)