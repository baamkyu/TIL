# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 

import sys
input = sys.stdin.readline

N = int(input())  # 지방의 수
arr = list(map(int, input().split()))  # 지방 별 필요한 예산
M = int(input())  # 총 예산


if sum(arr) < M:   # 필요한 예산이 총 예산보다 작은 경우
    print(max(arr))    
else:             # 필요한 예산이 총 예산보다 큰 경우 -> 배분이 필요함
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2  # 상한액 설정
        hap = 0
        for i in arr: 
            if i >= mid:          # 요청한 금액이 상한액 이상이라면 상한액 더하기
                hap += mid
            else:                 # 요청한 금액이 상한액 미만이라면 요청금액 더하기
                hap += i
        if hap <= M:  # 예산 금액이 총 예산 이하라면
            start = mid + 1
        else:         # 예산 금액이 총 예산 초과라면
            end = mid - 1
    print(end)  # 상한액이 곧 최대값