T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    box_list = []
    for i in range(len(box)):
        box_row = [] # box 안의 row
        for j in range(len(box)):
            box_row = [1]*box[i]+[0]*(M-box[i]) # box 안의 row들에 값을 넣어줌
        box_list.append(box_row) # row들을 append해서 2차원 리스트로 만듦

# 열에 박스가 몇개 있는지 확인하는 코드
    box_column = []
    for i in range(N):
        box_count = 0
        for j in range(M):
            box_count += box_list[j][i]
        box_column.append(box_count)

# 9-index-쌓여있는 박스개수 = 낙차 리스트
    drop_list = []
    for i in range(N):
        for j in range(M):
            if box_list[j][i] == 1:
                if 9-j-box_column[i] > 0:
                    drop_list.append(9-j-box_column[i])
    print(drop_list)

# 최대값 찾아내기
    max_drop = 0
    for i in drop_list:
        if i > max_drop:
            max_drop = i
    print(max_drop)