# N 이상 M 이하의 자연수 중 A*B로 유일하게 떨어지는 수의 개수를 구하라.
# A, B 는 2 이상의 자연수, A < B
N, M = map(int, input().split())

check = [0] * (M+1)
for i in range(2, int(M**0.5)+1):
    for j in range(i, M//i+1):
        if i * j >= N and i * j <= M:
          check[i*j] += 1
          
print(check.count(1))