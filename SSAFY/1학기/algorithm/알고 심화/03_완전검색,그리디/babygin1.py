'''
5
123123
124467
333444
444456
123444
'''

def f(i, k):
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0] + 1 == card[1] and card[1] + 1 == card[2]:
            run += 1
        if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
            run += 1
        if tri+run == 2:
            return 1
        else:
            return 0
    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            if f(i+1, k):   # return값이 1이면
                return 1    # 1출력 후 중단
            card[i], card[j] = card[j], card[i]
        return 0            # return값이 없으면 0출력



T = int(input())
for tc in range(1, T+1):
    card = list(map(int,input()))
    ans = f(0,6)    # babygin = 1, lose = 0 반환
    if ans:
        print(f'#{tc} BabyGin')
    else:
        print(f'#{tc} Lose')