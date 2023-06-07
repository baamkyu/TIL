# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

A, B = map(int, input().split())    # A, B 입력을 받고
if A > B:                           # A > B 인 경우
    print('>')                      # ">" 출력
elif A == B:                        # A 와 B가 같은 경우
    print('==')                     # "==" 출력
elif A < B:                         # A < B 인 경우
    print('<')                      # "<" 출력