# 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

N = input()

if len(N) == 1:   # input이 한자리이면 뒤에 0을 붙임
    N = N + '0'

num = N[1] + str(int(N[0]) + int(N[1]))[-1]
cnt = 1
while N != num:
    num = num[1] + str(int(num[0]) + int(num[1]))[-1]
    cnt += 1
print(cnt)