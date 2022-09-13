import sys
sys.stdin = open('SWEA1213_String.txt', 'r', encoding = 'UTF8') # encoding = 'UTF8'은 처음 보는 것!!

for tc in range(1, 11):  # 테스트 케이스는 10이라고 문제에 주어짐
    number = int(input())  # 테스트 케이스 번호 입력
    search = input()  # 찾을 문자열 입력
    S = input()  # 긴 문자열 입력
    count = 0
    for i in range(len(S)):  # 문자열 탐색
        if S[i:i+len(search)] == search:  # S 안에 search 문자열이 있으면 count+=1
            count+=1
    print(f'#{number} {count}')