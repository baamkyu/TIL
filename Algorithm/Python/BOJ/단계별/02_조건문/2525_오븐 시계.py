# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

hour, minute = map(int, input().split())    # 요리 시작하는 시각
need_time = int(input())                    # 요리하는데 걸리는 시각

temp = minute + need_time
if temp >= 60:
    hour += temp // 60
    minute = temp % 60
    if hour >= 24:
        hour -= 24
        print(hour, minute)
    else:
        print(hour, minute)
else:
    print(hour, temp)