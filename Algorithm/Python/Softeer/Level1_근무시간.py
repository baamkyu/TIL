import sys
input = sys.stdin.readline

ans = 0
for _ in range(5):
    s, e = input().split()
    shour, smin = s.split(':')
    ehour, emin = e.split(':')
    shour, smin, ehour, emin = int(shour), int(smin), int(ehour), int(emin)
    ans += (ehour - shour) * 60
    ans += (emin - smin)

print(ans)