import sys
sys.stdin = open('SWEA4865_글자수.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt_lst = [0] * len(set(str1))
    for i in range(len(set(str1))):
        for j in range(len(str2)):
            if list(set(str1))[i] == str2[j]:
                cnt_lst[i] += 1
        max_cnt_lst = max(cnt_lst)
    print(f'#{tc} {max_cnt_lst}')