  # N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하시오.

import sys
N = int(input())
nums = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    nums[num] += 1

# 리스트에서 1보다 큰 수가 있으면 인덱스를 수만큼 출력 
for i in range(10001):
    if nums[i] >= 1:
        for _ in range(nums[i]):
            print(i)