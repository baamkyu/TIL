T = int(input())  # 테스트케이스 수
for tc in range(1, T+1):
  arr = list(map(int, input().split()))
  print(sorted(arr)[-3])