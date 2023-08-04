import sys
input = sys.stdin.readline

W, N = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]
temp.sort(key=lambda x: x[1], reverse=True)

ans = 0
for weight, price in temp:
    if weight <= W:
        ans += weight * price
        W -= weight
    else:
        ans += W * price
        break
print(ans)