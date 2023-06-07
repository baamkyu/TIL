# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이

old_hour, old_minute = map(int, input().split())    # 기존 알람의 시각 입력
new_hour = 0
new_minute = 0
if old_minute < 45:                                 # 45분보다 작은 경우 시까지 변경해야 하므로
    new_minute = old_minute + 15                    # 기존 분 + 60분 - 45분
    if old_hour == 0:                               # 0시인 경우 23시로 변경
        new_hour = 23
    else:                                           # 0시가 아닌 경우 -1
        new_hour = old_hour - 1

elif old_minute >= 45:                              # 45분보다 크거나 같은 경우 시는 그대로, 분은 -45분
    new_hour = old_hour
    new_minute = old_minute - 45

print(new_hour, new_minute)
