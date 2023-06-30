# 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자.

def fib_rec(n):
    global cnt1
    if n == 1 or n == 2:
        return 1
    else:
        cnt1 += 1
        return fib_rec(n-1) + fib_rec(n-2)
    
def fib_dp(n):
    global cnt2
    f = [0] * 41
    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

N = int(input())

cnt1 = 1
cnt2 = 0

fib_rec(N)
fib_dp(N)

print(cnt1, cnt2)