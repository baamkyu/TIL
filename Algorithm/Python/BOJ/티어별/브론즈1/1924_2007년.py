# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?
x, y = map(int, input().split())
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']     # 요일 day of week

sum_day = 0
for i in range(x):
    sum_day += day[i]
sum_day += y
print(dow[sum_day % 7])