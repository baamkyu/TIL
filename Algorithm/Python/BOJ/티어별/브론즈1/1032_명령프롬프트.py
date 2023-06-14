N = int(input())
target = list(input())          # 첫번째 리스트 입력

for _ in range(N-1):
    compare = list(input())     # 비교할 리스트 입력
    for i in range(len(target)):
        if target[i] == compare[i]:
            pass
        else:       # 다른 글자이면 ?로 변환
            target[i] = '?'
print(''.join(target))