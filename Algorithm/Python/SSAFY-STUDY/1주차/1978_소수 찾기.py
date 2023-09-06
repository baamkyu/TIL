import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
no_prime_number = 0

for num in nums:
    if num == 1:
        no_prime_number += 1
    else:
        for i in range(2, num):
            if num % i == 0:
                no_prime_number += 1
                break
        
print(N - no_prime_number)