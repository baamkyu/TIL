# 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.

num = list(map(int, input().split()))
while num != [1, 2, 3, 4, 5]:
  for i in range(len(num)-1):
    if num[i] >= num[i+1]:
        tmp = 0
        tmp = num[i+1]
        num[i+1] = num[i]
        num[i] = tmp
        print(*num)

