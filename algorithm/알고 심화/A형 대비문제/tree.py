T = int(input())
for tc in range(1, T+1):
    N = int(input())
    given_tree = list(map(int, input().split()))
    subtract_list = []
    days = 0
    counting = {'odd': 0, 'even': 0, 'rest':0}

    max_height = max(given_tree)
    for i in range(N):
        if given_tree[i] < max_height:
            subtract_list.append(max_height - given_tree[i]) # 차이가 나면 차이가 얼마나 나는지 넣어준다. 다 쪽같으면 빈 리스트

    for i in range(len(subtract_list)):
        counting['odd'] += subtract_list[i]%2
        counting['even'] += subtract_list[i]//2

    while counting['odd'] > 0 or counting['even'] > 0 :
        days += 1 # 다음날이 되었습니다.
        if days % 2: # 홀수날이면
            if counting['odd'] == 0: # odd를 뺄 수 없어지면.. odd의 이틀이 even과 같아지는걸 카운팅해서 아쉽게라도 물을 통에 저장한다.
                counting['rest'] += 1
            else: # 홀수날이고 odd가 남아있다면
                counting['odd'] -= 1

            if counting['rest'] == 2:
                counting['rest'] -= 2
                counting['even'] -= 1
                if counting['odd'] == 0 and counting['even'] <= 0:  # 반례 2가 2개일 때.(1,2,3일에 물을 줘야함)
                    break

        else: # 짝수날이면, 이러면 even은 마이너스로 갈 수 있음. 근데 while조건을 부등호로 달았으니까 괜찮음. 귀찮아서 0밑으로 안내려가는 조건 안걸었음.
            counting['even'] -= 1
            continue

    print(f'#{tc} {days}')