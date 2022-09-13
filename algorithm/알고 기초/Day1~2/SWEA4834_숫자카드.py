import sys
sys.stdin = open('input_4834.txt')

T = int(input()) # 테스트케이스 개수 입력
for tc in range(1, T+1): # 테스트케이스 개수동안 도는 for문
    N = int(input()) # tc번째 테스트케이스의 길이 입력
    card_data = int(input()) # 테스트케이스 데이터 입력
    card_list = [] # 카드의 값 리스트
    cnt = [0]*10 # 카드 개수 리스트
    max_cnt = cnt[0]

    for n in range(N): # 테스트케이스의 마지막 글자를 card_list에 추가
        card_list.append(card_data % 10)
        card_data = card_data // 10
    print(card_list) # %와 //를 이용해 카드의 값을 리스트로 만듦

    for i in range(len(card_list)): # 카드의 개수만큼 for문
        cnt[card_list[i]] += 1 # 카드의 개수만큼  표시
        if max_cnt < cnt[card_list[i]]: # 카드의 개수가 가장 큰 값을 max_cnt에 넣어줌
            max_cnt = cnt[card_list[i]]
            many_card_value = card_list[i] # 개수가 가장 많은 카드의 수를 many_card에 대입

        if max_cnt == cnt[card_list[i]] and many_card_value < card_list[i]:

            many_card_value = card_list[i]


    print(f'#{tc} {many_card_value} {max_cnt}')
