def solution(s):
    s = s.split(' ')
    new_arr = []
    answer = ''
    for i in range(len(s)):
        if s[i] == '':
            pass
        else:
            new_arr.append(s[i][0].upper()+s[i][1:].lower())
        answer = ' '.join(new_arr)
    return answer
print(solution('for  34the  last w eek'))