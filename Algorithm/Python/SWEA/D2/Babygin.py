# Babygin
# 문제 : 0~9 사이의 카드가 있고 복원추출로 임의의 카드를 6번 뽑았을 때
# 3장의 카드가 연속된 숫자가 나오면 run, 3장의 카드가 동일하게 나오면 triplet이다.
# run과 triplet으로 구성된 경우를 baby-gin으로 부른다. baby-gin인지 판단하는 프로그램을 작성하라.

num = list(map(int, input()))
arr = [0]*9
answer = 0  # run 혹은 triplet의 개수
for i in num:
  arr[i] += 1
  if arr[i] == 3: # 한가지 숫자가 3개 나온 경우
    arr[i] -= 3   
    answer += 1
for i in range(8):
  if arr[i] >= 1:
    if arr[i] == arr[i+1] == arr[i+2]:
      if arr[i] == 1:
        answer += 1
      elif arr[i] == 2:
        answer += 2
if answer == 2:
  print('babygin')
else:
  print('no')