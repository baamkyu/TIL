T = 10
for tc in range(1, 11):
    N = int(input())    # 회문 찾을 글자 수
    data = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):      # 가로 회문 찾기
        for j in range(8-N+1):
            if data[i][j:j+N] == data[i][j:j+N][::-1]:
                cnt += 1
# for문으로 90도 회전
    tmp_data = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            tmp_data[i][j] = data[8-j-1][i]

# # zip 사용해서 90도 회전
#     tmp_data = list(zip(*data[::-1]))


    for i in range(8):      # 세로 회문 찾기
        for j in range(8-N+1):
            if tmp_data[i][j:j + N] == tmp_data[i][j:j + N][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')

# 90도 : rotated_matrix = list(zip(*matrix[::-1]))
# -90도 : rotated_matrix = list(zip(*matrix))[::-1]
# 전치 : zipped_matrix = list(zip(*matrix))