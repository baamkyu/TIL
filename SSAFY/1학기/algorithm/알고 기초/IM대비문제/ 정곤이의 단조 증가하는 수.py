T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    gop_lst = []
    for i in range(N-1):      # 두 수의 모든 곱을 담은 리스트 생성
        for j in range(i+1, N):
            gop_lst += [data[i] * data[j]]

    str_gop_lst2 = []
    for i in gop_lst:
        str_gop_lst = str(i)
        for j in range(len(str_gop_lst)-1):
            if str_gop_lst[j] <= str_gop_lst[j+1]:
                pass
            else:
                break
        else:
            str_gop_lst2 += [i]

    if str_gop_lst2:
        max_ans = max(str_gop_lst2)
    else:
        max_ans = -1
    print(f'#{tc} {max_ans}')

    #1 pop -> 점점 작아지는지
    #2 int






    # for i in range(len(gop_lst)):   # 단조 증가하는 수인지 확인
    #     for j in range(len(str(gop_lst[i]))-1):
    #         if gop_lst[i] // 10** (len(str(gop_lst[i]))-1) < gop_lst[i] % 10**(len(str(gop_lst[i]))-1):
    #             ans_lst.append(gop_lst[i])
    #             print(ans_lst)
    # max_ans_lst = max(ans_lst)
    # print(f'#{tc} {max_ans_lst}')