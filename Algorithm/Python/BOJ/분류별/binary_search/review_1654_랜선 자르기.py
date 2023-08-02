import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

s, e = 1, max(lans)
while s <= e:
    mid = (s+e) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
print(s, e, mid)