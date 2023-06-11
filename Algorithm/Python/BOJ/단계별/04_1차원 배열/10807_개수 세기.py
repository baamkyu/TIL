# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

N = int(input())
arr = list(map(int, input().split()))
count = 0
v = int(input())
for i in range(N):
    if arr[i] == v:
        count += 1
print(count)