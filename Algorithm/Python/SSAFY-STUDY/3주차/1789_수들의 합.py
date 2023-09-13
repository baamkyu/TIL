import sys
input = sys.stdin.readline

S = int(input())
N = 0
ans = 0
for i in range(1, S+1):
    ans += i
    N += 1
    if ans > S:
        N -= 1
        break
print(N)