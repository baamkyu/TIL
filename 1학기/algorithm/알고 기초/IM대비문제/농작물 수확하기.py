T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 농작의 크기
    value = [list(map(int,input())) for _ in range(N)]# 농작물의 가치 입력
    value_lst = []
    k = N//2    # 계산을 간단하게 하기 위해 임의로 생성
    for i in range(N):  # 리스트에 추가
        value_lst.append(value[i][abs(i-k):N-abs(i-k)])

    value_hap = 0
    for i in range(len(value_lst)):     # 리스트의 값들을 다 더해줌
        for j in range(len(value_lst[i])):
            value_hap += value_lst[i][j]
    print(f'#{tc} {value_hap}')