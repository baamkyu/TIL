# N자리 16진수가 주어지면 각 자리수를 4자리 2진수로 표시하는 프로그램
'''
3
4 47FE
5 79E12
8 41DA16CD
'''

# text[i]를 16->10->2진수로 변경, 길이에 따라 앞에 0 추가

T = int(input())
for tc in range(1, T+1):
    N, text = input().split()
    temp = 0
    ans = ''
    real_ans = ''
    for i in range(int(N)):
        temp = bin(int(text[i], 16))[2:]
        ans = '0'*(4 - len(temp)) + temp
        real_ans += ans
    print(f'#{tc} {real_ans}')
