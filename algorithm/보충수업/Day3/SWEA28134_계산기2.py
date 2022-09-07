import sys
sys.stdin = open('SWEA28134_계산기2.txt', 'r')

pri = {'+': 1, '*' : 2}
T = 10
for tc in range(1, T+1):
    N = input()
    string = input()    # 중위표기식 입력
    equ = ''
    stk = []

    # 1. 중위표기식 -> 후위표기식
    for ch in string:
        if ch.isdigit():
            equ += ch
        else:
            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)
    while stk:
        equ += stk.pop()

    # print(equ)

    # 2. 후위표기식 계산
    # 숫자면 stk에, 연산자면 2개 pop해서 연산(우선순위 주의)
    ans = 0
    for ch in equ:
        # if '0' <= ch <= '9' # list인 경우
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '+':
                stk.append(op1 + op2)
            if ch== '*':
                stk.append(op1 * op2)

    print(f'#{tc} {stk[-1]}')