# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] = max(arr[i], arr[i-1] + arr[i])
print(max(arr))

# 풀이방법 : arr[i] = arr[i-1] + arr[i] or arr[i] => 연속해서 더한 값과 새로 시작한 값을 비교해서 더 큰 수로 초기화!
# 이 중 최대값을 출력하면 연속된 수 중 가장 큰 수가 된다.