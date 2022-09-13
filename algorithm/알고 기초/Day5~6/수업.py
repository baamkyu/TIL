# greeting = 'abc'
# a = list(reversed(greeting))
# reversed_greeting = ''.join(list(reversed(greeting)))   # 문자열 뒤집기
# print(a)
# print(reversed_greeting)


# .sort와 sorted 차이
# .sort = 원본이 바뀜
# sorted = 할당을 해줘야함

# s='123'
# a = atoi(s)
# print(a)

# itoa
# def itoa(int_num):
#     str_num = ''
#
#     while int_num:
#         str_num = chr(int_num % 10 + 48) + str_num # 끝부분 뗀 것
#         int_num //+10
#     return str_num
# print(itoa(1234), type(itoa(1234)))




# #atoi
# def atoi(str_num):
#     int_num = 0
#
#     for i in str_num:
#         int_num += 10
#         int_num += (ord[i] - 48)
#
#     return int_num
#
# print(atoi('1234'))
#
#
#
# # .find
# a = 'hello'
# a.find('ll')
# if 'll' in 'hello':
#     print('찾았다')


def bruteforce(p, t):
    N=len(t)
    M=len(p)

    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j]==p[j]:
                cnt+=1
            else:
                break

        if cnt==M:
            return '찾았다'
    return '못찾았다'

print(bruteforce('hel', 'hello'))