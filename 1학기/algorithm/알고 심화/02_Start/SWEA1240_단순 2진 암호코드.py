T = int(input())
dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T+1):
    N, M = map(int,input().split())     # 세로 N, 가로 M

    arr = [input() for _ in range(N)]   # N*M 배열 input

    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                idx_i = i
                idx_j = j
                break

    code = arr[idx_i][idx_j-55:idx_j+1]     # 암호로 사용할 code (N * 7개)

    code_lst = []
    for i in range(0, 56, 7):               # 암호를 7글자씩 나눠줬음
        code_lst.append(code[i:i+7])
    # print(code_lst)

    ans_lst = []
    for i in range(len(code_lst)):         # 암호해독
        ans_lst.append(dic[code_lst[i]])
    # print(ans_lst)

    hol = 0
    zzak = 0
    for i in range(7//2+1):
        hol += ans_lst[i*2]
        zzak += ans_lst[i*2+1]

    if ((hol*3 + zzak) % 10) == 0:  # 올바른 암호코드인 경우
        print(f'#{tc}', end = ' ')
        print(sum(ans_lst))
    else:   # 잘못된 암호코드인 경우 0 출력
        print(f'#{tc}', end=' ')
        print(0)