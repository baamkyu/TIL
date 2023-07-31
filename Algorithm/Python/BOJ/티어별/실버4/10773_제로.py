import sys
input = sys.stdin.readline

K = int(input())
temp = []
for _ in range(K):
    n = int(input())
    if n != 0:
        temp.append(n)
    else:
        temp.pop()
print(sum(temp))