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

month_list = [['january', 1], ['february', 2], ['march', 3], ['april', 4], ['may', 5], ['june', 6], 
                  ['july', 7], ['august', 8], ['september', 9], ['october', 10], ['november', 11], ['december', 12]]
day_list = [['sunday', 1], ['monday', 2], ['tuesday', 3], ['wednesday', 4], ['thursday', 5], ['friday', 6], ['saturday', 7]]
    
if isLeap == 'leap':
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(N):
    num, day, trash, month = map(str, input().split())

# 매달 첫번째 요일 구하기
firstday_of_month = [0] * 12
for i in day_list:
    if firstDay == i[0]:
        firstday_of_month[0] = i[1]
        break

for i in range(1, 12):
    firstday_of_month[i] = (firstday_of_month[i-1] + month_day[i] % 7) % 7


# 며칠인지 구하기
for i in day_list:
    if i[0] == day:
        if i[1] < firstday_of_month[]:   # 찾는 요일이 시작일보다 전일때
          int(day) 