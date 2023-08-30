# 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if ans == M:
                break
            if nums[i] + nums[j] + nums[k] <= M and nums[i] + nums[j] + nums[k] > ans:
                ans = nums[i] + nums[j] + nums[k]
print(ans)