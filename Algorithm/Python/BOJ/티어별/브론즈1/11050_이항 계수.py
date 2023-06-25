# n과 k가 주어졌을 때 nCk를 구하여라

def bin(n, k):
    parent = 1
    child = 1
    for i in range(n, n-k, -1):
        parent = i * parent
    
    for i in range(1, k+1):
        child = i * child
    return parent // child

N, K = map(int, input().split())
print(bin(N, K))
        