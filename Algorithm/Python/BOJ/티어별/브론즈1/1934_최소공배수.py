# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하라.

# 풀이방법 : 유클리드 호제법 사용
# 최대공약수
def gcd(a, b):
    while b != 0:
       a, b = b, a % b
    return a

# 최소공배수
def lcm(a, b):
    i = gcd(a, b)
    return a * b // i

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))