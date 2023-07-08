N = int(input())
nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
nums.sort()
for i in nums:
    print(i)