# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i-1]

ans = -9999
for i in range(K, N):
    if ans > arr[i] - arr[i-K]:
        ans = arr[i] - arr[i-K]
print(ans)