def isbabygin(card):
    for i in range(8):
        if card[i] and card[i+1] and card[i+2]:
            return True
    for i in range(10):
        if card[i] == 3:
            return True
    return False



T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    player1 = [0] * 10  # 0 ~ 9 까지의 카드를 담아줄 빈 리스트 생성
    player2 = [0] * 10

    ans = 0
    for i in range(6):      # 전체 카드가 12개 (플레이어당 6개씩 부여함)
        player1[temp[i*2]] += 1
        if isbabygin(player1):      # return값이 True이면
            ans = 1                 # 승자가 정해지면 break
            break
        player2[temp[i * 2 + 1]] += 1
        if isbabygin(player2):    # return값이 True이면
            ans = 2                 # 승자가 정해지면 break
            break
    print(f'#{tc} {ans}')