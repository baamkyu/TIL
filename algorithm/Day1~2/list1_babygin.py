N = int(input())
for tc in range(1, N+1):
    arr = list(map(int, input()))
    c = [0]*10
    score = 0 # 2가 되면 babygin으로 판정
    for i in range(len(arr)): #카운팅 정렬
        c[arr[i]] += 1
    for i in range(0, len(c)-2):
        if c[i]>0 and c[i]==c[i+1]==c[i+2]==1: #3개의 수가 연속되면 score+=1
            score+=1
        elif c[i]>0 and c[i]==c[i+1]==c[i+2]==2: #3개의 수가 두번씩 연속되면 score=2
            score=2
    for i in range(0, len(c) - 5):
        if c[i] == c[i + 1] == c[i + 2] == c[i + 3] == c[i + 4] == c[i + 5]:  # 6개의 수가 연속되면 score+=2
            score = 2
    for i in range(0, len(c)):
        if c[i]>=3: #3개의 수가 같으면 score+=1
            score+=1
        elif c[i]==6: #6개의 수가 같으면 score+=2
            score=2

    if score==2:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
