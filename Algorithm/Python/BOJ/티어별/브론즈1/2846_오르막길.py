# 가장 큰 오르막길을 구하는 프로그램을 작성하시오.

N = int(input())
road = list(map(int, input().split()))
up_list = [0]   # 오르막길 리스트
up = 0          # 오르막길 크기
for i in range(N-1):
    if road[i] < road[i+1]:
        up += road[i+1] - road[i]
        up_list.append(up)
    else:
        up = 0
print(max(up_list))