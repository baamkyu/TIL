# 다음 두 가지 요금제 중 하나를 선택하라고 한다.
# 1. 영식 요금제 (=Y로 출력) 2. 민식 요금제 (=M으로 출력)
# 영식 요금제 : 30초마다 10원씩 ex. 31초 -> 20원
# 민식 요금제 : 60초마다 15원씩 ex. 59초 -> 15원, 60초 -> 30원
# 두 요금제의 요금이 같으면 영식을 먼저 쓰고 민식을 그 다음에 쓴다

N = int(input())
call_time = list(map(int, input().split()))
M_money = 0
Y_money = 0
for i in call_time:
  if i == 0:    # 통화를 하지 않았으면 요금 부과 No
    pass
  else:
    Y_money += i // 30 * 10 + 10  # 영식 요금제를 사용한 경우 요금 계산
    M_money += i // 60 * 15 + 15  # 민식 요금제를 사용한 경우 요금 계산
if Y_money > M_money:     # 민식 요금제가 더 싼 경우
  print('M', M_money)
elif Y_money < M_money:   # 영식 요금제가 더 싼 경우
  print('Y', Y_money)
elif Y_money == M_money:  # 민식 요금제, 영식 요금제 가격이 같은 경우
  print('Y M', Y_money)