import sys

K, N = map(int, input().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    cnt = 0   # 랜선 수
    for lan in lans:
        cnt += lan // mid   # 분할된 랜선 수 추가
    
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)