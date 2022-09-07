## 피노나치 수열 이용 -> 느림, 컴퓨터 부하
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
# for i in range(1, 101):
#     print(i, fibo(i))

## memoization를 활용해 이용 -> 더 빠름
# def fibo(n):
#     if n >= 2 and memo[n] == 0:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
# memo = [0]*101
# memo[0] = 0
# memo[1] = 1
# for i in range(1, 101):
#     print(i, fibo(i))


## 피보나치 수열 DP적용 알고리즘
def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return

table = [0]*101
fibo_dp(100)
print(table)