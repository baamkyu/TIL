T = int(input())
for tc in range(1, T+1):
    bit = list(map(int, input()))
    len_bit = len(bit)
    arr = [0] * len_bit
    cnt_first1 = 1                      # 맨 앞의 수가 1일 때
    cnt_first0 = 0                      # 맨 앞의 수가 0일 때
    for i in range(len_bit-1):
        if bit[0] == 1:
            if bit[i] != bit[i+1]:      # 앞 뒤 수가 다를 때마다 cnt+=1
                cnt_first1 += 1
        if bit[0] == 0:
            if bit[i] != bit[i+1]:
                cnt_first0 += 1
    cnt = max(cnt_first0, cnt_first1)

    print(f'#{tc} {cnt}')