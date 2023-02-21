def isbabygin(card):
    for i in range(8):
        if card[i] and card[i+1] and card[i+2]:     # 세개 연속으로 값이 있으면
            return True     # run이므로 true
    for i in range(10):
        if card[i] == 3:
            return True     # triplet이므로 true

    return False            # 둘 다 아니면 False

T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    ans = 0
    player1_count = [0] * 10    # 0 ~ 9 까지의 수를 카운트
    player2_count = [0] * 10

    for i in range(len(temp)//2):
        player1_count[temp[i*2]] += 1       # 수에 맞게 += 1
        if isbabygin(player1_count):        # True면 player1이 이김
            ans = 1
            break

        player2_count[temp[i*2+1]] += 1
        if isbabygin(player2_count):        # True면 player2가 이김
            ans = 2
            break

    print(f'#{tc} {ans}')