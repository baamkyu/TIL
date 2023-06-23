# 정수 N이 주어졌을 때, 소인수분해하시오.

N = int(input())
i = 2
if N <= 1:
    print('')
else:
    while N != 1:
        if N % i == 0:
            print(i)
            N = N // i
        else:
            i += 1
