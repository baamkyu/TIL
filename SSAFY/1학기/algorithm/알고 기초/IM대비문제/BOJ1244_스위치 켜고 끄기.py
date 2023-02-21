how_many_switch = int(input())  # 스위치의 개수 입력
switch = list(map(int, input().split()))  # 스위치의 상태 입력
how_many_student = int(input())  # 학생 수 입력
for student in range(how_many_student):
    gender, number = map(int, input().split())  # 학생 수만큼 성별, 받은 수 입력
# 남자일 때
    for i in range(1, len(switch)+1):
        if gender == 1 and (number*i)-1 < len(switch):
            if switch[(number*i)-1] == 0:
                switch[(number*i)-1] = 1
            elif switch[(number*i)-1] == 1:
                switch[(number*i)-1] = 0
            else:
                continue
        else: continue

# 여자일 때
    for j in range(0, len(switch)//2+1):
        # j가 0부터 필요해서 for문을 따로 하나 더 만들어줌
        if gender == 2 and switch[number+j-1] == switch[number-j-1] and (number + j) < len(switch) and (number - j) > 0:
            if switch[number+j-1] == 0:
                switch[number+j-1] = 1
                switch[number-j-1] = 1
            elif switch[number-j-1] == 1:
                switch[number+j-1] = 0
                switch[number-j-1] = 0
        # if number + j > len(switch) or number - j < 0:
        #     break

print(*switch)
# if 남학생(1), 자기의 번호 배수의 스위치를 바꾼다. (3을 받았으면, 3, 6을 바꾼다)
# if 여학생(2), 번호+0, -0 : 바꿈, 번호+1 == 번호-1 : 바꿈, 번호+2 == 번호-2 : 바꿈

# 스위치개수 입력
# 스위치상태 입력
# 학생수 입력
# 성별 받은 수 입력
# 성별 받은 수 입력


# N_switch = int(input())
# switch_list = list(map(int, input().split()))
#
# N = int(input())
# for _ in range(N):
#     gender, num = map(int, input().split())
#
#     # 남자
#     if gender == 1:
#         for i in range(len(switch_list)):
#             # 배수 판별
#             # print((i+1)%A[1])
#             if not (i + 1) % num:  # i+1이 스위치 번호
#                 # 값 전환
#                 if switch_list[i] == 1:
#                     switch_list[i] = 0
#                 elif switch_list[i] == 0:
#                     switch_list[i] = 1
#
#     # 여자
#     if gender == 2:
#         # 대칭 확인
#         for i in range(num):
#             # print(num+i-1==num-i-1)
#             if switch_list[num + i - 1] == switch_list[num - i - 1]:  # 스위치 번호가 인덱스보다 1크다 그래서 -1
#                 # 값 전환
#                 if switch_list[num + i - 1] == 1:
#                     switch_list[num + i - 1] = 0
#                     switch_list[num - i - 1] = 0
#                 elif switch_list[num + i - 1] == 0:
#                     switch_list[num + i - 1] = 1
#                     switch_list[num - i - 1] = 1
#
# print(*switch_list)













# S = int(input())
# switch = [0]+list(map(int, input().split()))
# P = int(input())
#
#
# def change(i):
#     if switch[i] == 0:
#         switch[i] = 1
#     else:
#         switch[i] = 0
#
#
# for i in range(P):
#     gen, num = map(int, input().split())
#     if gen == 1:
#         for i in range(num, S+1, num):
#             change(i)
#     else:
#         if num+1 > S or num-1 < 1:
#             change(num)
#         else:
#             if switch[num-1] == switch[num+1]:
#                 left = num-1
#                 right = num+1
#                 while True:
#                     if left-1 < 1 or right+1 > S:
#                         break
#                     if switch[left-1] != switch[right+1]:
#                         break
#                     else:
#                         left -= 1
#                         right += 1
#                 for i in range(left, right+1):
#                     change(i)
#             else:
#                 change(num)
# for i in range(1, S+1, 20):
#     print(*switch[i:i+20])
