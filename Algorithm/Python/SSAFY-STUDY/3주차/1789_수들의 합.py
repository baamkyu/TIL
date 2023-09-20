import sys
input = sys.stdin.readline

S = int(input())

N = 0
num_sum = 0
for i in range(1, S+1):
    N += 1
    num_sum += i
    if num_sum > S:
        N -= 1
        break
print(N)