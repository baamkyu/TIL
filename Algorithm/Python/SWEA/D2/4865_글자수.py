T = int(input())
for tc in range(1, T+1):
  set_word = list(set(input())) # 첫번째 인풋을 중복제거해줌
  check = [0]*len(set_word)
  input_word = list(input())   # 두번째 인풋
  print(input_word)
  for i in range(len(set_word)):
    for j in input_word:
      if j == set_word[i]:
        check[i] += 1
  print(f'#{tc} {max(check)}')