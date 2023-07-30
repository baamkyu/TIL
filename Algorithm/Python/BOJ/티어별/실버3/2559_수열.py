# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 첫번째 K까지의 합
ans = [sum(arr[:K])]

# ans[-1] == K개의 합 이니까 다음 K개의 합을 구하려면 arr[i]을 빼고 arr[i+K]를 더해주면 됨
for i in range(N-K):
    ans.append(ans[-1]-arr[i]+arr[i+K])
print(max(ans))