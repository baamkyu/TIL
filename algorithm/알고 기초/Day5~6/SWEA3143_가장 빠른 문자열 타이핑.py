#1. 내장함수 count 사용
T = int(input())  # test case 개수 입력
for tc in range(1, T+1):
    S, small_S = map(str, input().split())
    cnt = len(S)
    if small_S in S:
        how_many_small_S = S.count(small_S)
        cnt = cnt - len(small_S)*how_many_small_S + how_many_small_S  # small_S에 있는 문자열의 길이를 빼주고 1을 더해 한글자로 인식한다
    print(f'#{tc} {cnt}')

#2. 내장함수 replace 사용
T = int(input())
for tc in range(1, T+1):
    S, small_S = map(str, input().split())
    S.replace(small_S, '*')  # small_S에 있는 문자열을 *로 변환한다
    print(f'#{tc} {len(S)}')