# 어느 나라의 공휴일을 정하려고 한다.
# 첫째줄에는 공휴일의 수, 둘째줄에는 윤년 여부, 셋째줄에는 1월 1일의 요일, 넷째줄부터는 공휴일을 알려준다.

# 5
# non-leap
# monday
# first tuesday of january
# second saturday of january
# third sunday of march
# last monday of april
# fourth wednesday of october

# 4
# leap
# tuesday
# second tuesday of january
# fourth saturday of january
# third sunday of march
# last monday of april

N = int(input())
isLeap = input()
firstDay = input()

month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
week_list = ['first', 'second', 'third', 'fourth', 'last']

if isLeap == 'leap':
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 매달 첫번째 요일 구하기
firstday_of_month = [0] * 12

# 1월 1일의 요일
firstday_of_month[0] = day_list.index(firstDay)
# 2월 ~ 12월 1일의 요일
for i in range(1, 12):
    firstday_of_month[i] = (firstday_of_month[i-1] + month_day[i-1] % 7) % 7

# print(firstday_of_month)



for _ in range(N):
    num, day, _, month = input().split()

    ans_mon = month_list.index(month)+1

    # 그 달의 1일 요일과 구하려는 요일 비교
    if day_list.index(day) < firstday_of_month[month_list.index(month)]:
        ans_day = day_list.index(day) - firstday_of_month[month_list.index(month)] + 1 + (week_list.index(num)+1) * 7
        if ans_day > month_day[ans_mon - 1]:
            ans_day -= 7
        print(ans_mon, ans_day)
    else:
        ans_day = day_list.index(day) - firstday_of_month[month_list.index(month)] + 1 + (week_list.index(num)) * 7
        print(ans_mon, ans_day)


# 운창님 코드
# N = int(input())
# yooncal = (31,29,31,30,31,30,31,31,30,31,30,31)
# noyooncal = (31,28,31,30,31,30,31,31,30,31,30,31)
# prio_list = ('first', 'second', 'third', 'fourth', 'last')
# month_list = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
# day_list = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
# mycal = yooncal if input()=="leap" else noyooncal
# firstday = input()
# idx = day_list.index(firstday)
# for _ in range(N):
#     prio, day, _, mon = input().split()
#     prioval = prio_list.index(prio)
#     monval = month_list.index(mon)
#     dayval = day_list.index(day)
#     temp = idx
#     if monval: # 2월 이상
#         temp += sum(mycal[:monval])
#         temp %= 7
#         boost = 0
#         while temp%7 != dayval:
#             temp += 1
#             boost += 1
#         temp = boost + 1
#         temp += prioval*7
#         if temp > mycal[monval]:
#             temp -= 7
#         print(monval+1, temp)
#     else: # 1월
#         temp_list = day_list[idx:] + day_list[:idx]
#         dayval = temp_list.index(day)
#         while temp != dayval:
#             temp += 1
#             temp %= 7
#         temp += prioval*7
#         if temp > 31:
#             temp -= 7
#         print(1, temp+1)