# 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다.
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, max(arr)
while s <= e:
    tree = 0
    mid = (s+e) // 2
    for i in arr:
        if i >= mid:
            tree += i - mid
    if tree < M:
        e = mid - 1
    else:
        s = mid + 1
print(e)