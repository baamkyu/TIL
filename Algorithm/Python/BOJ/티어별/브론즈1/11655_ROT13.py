# ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.

S = input()
ans = ''
for i in range(len(S)):
    if ord(S[i]) >= 65 and ord(S[i])<=90 or ord(S[i]) >= 97 and ord(S[i]) <= 122: # 대문자 혹은 소문자인 경우
      if ord(S[i]) + 13 > 122:                      # 소문자 유지
          ans += chr(96 + (ord(S[i]) + 13) - 122)
      elif ord(S[i]) + 13 > 90 and ord(S[i]) <= 90: # 대문자 유지
          ans += chr(64 + (ord(S[i]) + 13) - 90)
      else:
          ans += chr(ord(S[i]) + 13)
    else:     # 대문자 혹은 소문자가 아닌 경우 그대로 둔다
        ans += chr(ord(S[i]))
print(ans)