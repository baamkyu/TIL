# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.

import sys
input = sys.stdin.readline

N = int(input())
ans = 99

if N < 100:
    print(N-1)
else:
    for i in range(100, N+1):
        num_list = list(map(int, str(i)))
        if num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            ans += 1
    print(ans)