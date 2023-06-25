# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다.
# 주어진 수의 팰린드롬 수 여부를 확인하라.

while True:
  n = list(map(int, input()))
  if n == [0]:
      break
  if n == n[::-1]:
      print('yes')
  else:
      print('no')