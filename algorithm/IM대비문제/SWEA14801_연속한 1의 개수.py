import sys
sys.stdin = open('SWEA14801_연속한 1의 개수.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    seq = input()
    cnt = 0
    cnt_lst = []
    for i in range(0, N):
        if seq[i] == '1':
            cnt += 1
            cnt_lst.append(cnt)
        else:
            cnt = 0
            cnt_lst.append(cnt)

    max_cnt_lst = cnt_lst[0]
    for j in range(len(cnt_lst)):
        if max_cnt_lst < cnt_lst[j]:
            max_cnt_lst = cnt_lst[j]

    print(f'#{tc} {max_cnt_lst}')