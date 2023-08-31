import sys
input = sys.stdin.readline

N = int(input())
ans = 0


for i in range(1, N):
    dec = i
    for j in str(i):
        dec += int(j)
    if dec == N:
       ans = i
       break
print(ans)