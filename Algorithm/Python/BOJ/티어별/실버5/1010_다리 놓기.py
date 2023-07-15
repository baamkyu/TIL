
# nCr = n! // (n-r)!r!

def fact(n):
    if n > 1:
        return (n * fact(n-1))
    else:
        return 1
    
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(fact(M) // (fact(M-N) * fact(N)))