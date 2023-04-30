# 숫자는 스택에 넣는다.
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# ‘.’은 스택에서 숫자를 꺼내 출력한다.
# Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오.
# 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

T = int(input())

for tc in range(1, T+1):
    target = input().split()
    stack = []  # 숫자를 담을 리스트
    answer = 0  # 정답을 담을 변수
    symbol = ['-', '+', '/', '*']
    
    for i in target:
        if i == '.':
            if len(stack) != 1:     # .을 만났지만 안에 2개 이상 있으면 그것은 에러
                answer = 'error'
                break
            answer = stack.pop()    # 마지막 하나 남았을 때는 그것이 정답임

        elif i not in symbol:       # 숫자인 경우 stack에 쌓는다
            stack.append(int(i))

        elif i in symbol:
            if len(stack) < 2:      # 스택에 숫자가 한개이하면 연산 불가 -> 에러
                answer = 'error'
                break
            last_one = stack.pop()
            last_two = stack.pop()

            if i == '-':
                stack.append(last_two - last_one)
            elif i == '+':
                stack.append(last_two + last_one)           
            elif i == '*':
                stack.append(last_two * last_one)
            elif i == '/':
                stack.append(last_two // last_one)

    print(f'#{tc} {answer}')
