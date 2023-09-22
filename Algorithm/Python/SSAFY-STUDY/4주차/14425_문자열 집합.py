import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
tmp = dict()

for i in range(n):
    index = input().strip()
    tmp[index] = True

for j in range(m):
    check = input().strip()
    if check in tmp:
        cnt += 1
print(cnt)