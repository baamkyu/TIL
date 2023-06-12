# 규칙
# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

while True:
  N = input()
  if N == '0':
      break
  else:
      num_list = list(map(int, N))
  answer = 2  # 양 옆의 공백 1씩을 미리 더해줌
  for i in num_list:
      answer += 1     # 글자 사이의 여백
      if i == 1:      # 1인 경우 너비 2
          answer += 2
      elif i == 0:    # 0인 경우 너비 4
          answer += 4
      else:           # 나머지 숫자는 3
          answer += 3
  print(answer - 1)   # 글자 사이의 총 여백은 글자가 3개이면 여백=2이기 때문에 마지막에 -1해줌