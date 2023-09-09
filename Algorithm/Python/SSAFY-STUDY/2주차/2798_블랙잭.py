N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if nums[i] + nums[j] + nums[k] > M:
                pass
            else:
                if ans < nums[i] + nums[j] + nums[k]:
                    ans = nums[i] + nums[j] + nums[k]
print(ans)
