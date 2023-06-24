N = int(input())

if N == 0:      # fibo(0) = 0
    print(0)
elif N == 1:    # fibo(1) = 1
    print(1)
else:
    n1 = 0
    n2 = 1
    for i in range(2, N+1):   # fibo(0) = 0, fibo(1) = 1 이기 때문에 fibo(2)부터 계산
        fibo = n1 + n2
        n1 = n2
        n2 = fibo
        if i == N:
            print(fibo)