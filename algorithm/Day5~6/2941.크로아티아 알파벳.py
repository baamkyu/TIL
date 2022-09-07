#1
cro_alpha = ['c=', 'c', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
for i in cro_alpha:
    if i in S: # 입력받은 문자열 안에 크로아티아 알파벳이 있으면
        S = S.replace(i, '@')  # 크로아티아 알파벳에 해당하는 것은 @로 변환
print(S)
print(len(S))

#2
S = list(input())
print(S)
count = 0
for i in range(0, len(S)-1):
    if S[i] == 'c' and S[i+1] == '=':
        count -= 1
    elif S[i] == 'c' and S[i+1] == '-':
        count -= 1
    elif S[i] == 'd' and S[i+1] == 'z' and S[i+2] == '=':
        count -= 1
    elif S[i] == 'l' and S[i+1] == 'j':
        count -= 1
    elif S[i] == 'n' and S[i+1] == 'j':
        count -= 1
    elif S[i] == 's' and S[i+1] == '=':
        count -= 1
    elif S[i] == 'z' and S[i+1] == '=':
        count -= 1
print(len(S) + count)


cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
for i in cro_alpha:
    if i in S:
        S = S.replace(i, '*')
print(len(S))

