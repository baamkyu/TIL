import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(str, input()))

check = [0] * (N+1)

for i in range(N):
    if arr[i] == 'P':
        if i-K < 0 and i+K+1 > N:
            for j in range(0, N):
                if arr[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    break
        elif i-K < 0:
            for j in range(0, i+K+1):
                if arr[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    break
        elif i+K+1 > N:
            for j in range(i-K, N):
                if arr[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    break
        else:
            for j in range(i-K, i+K+1):
                if arr[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    break
print(sum(check))