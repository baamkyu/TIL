# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오.

# 2차원 배열 입력
N, M = map(int, input().split())  # 배열의 크기
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

K = int(input())
for _ in range(K):
    ans = 0
    find = list(map(int, input().split()))  # 합을 구할 부분 입력
    for i in range(find[0]-1, find[2]):
      for j in range(find[1]-1, find[3]):
          ans += arr[i][j]
    print(ans)