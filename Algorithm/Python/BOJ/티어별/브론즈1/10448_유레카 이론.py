# 자연수 n에 대해 n ≥ 1의 삼각수 Tn는 명백한 공식이 있다.
# Tn = 1 + 2 + 3 + ... + n = n(n+1)/2
# 1796년, 가우스는 모든 자연수가 최대 3개의 삼각수의 합으로 표현될 수 있다고 증명하였다.

# 주어진 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 
# 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

Tn = [n*(n+1)//2 for n in range(1, 45)]     # 삼각 수로 이루어질 수 있는 모든 값들

check = [0] * 1001  # 3 <= N <= 1000이기 때문에
for i in Tn:
    for j in Tn:
        for k in Tn:
            if i + j + k <= 1000:
                check[i+j+k] = 1

T = int(input())
for _ in range(T):
    n = int(input())

    print(check[n])