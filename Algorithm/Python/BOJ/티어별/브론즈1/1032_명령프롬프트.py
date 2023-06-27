# N = int(input())
# target = list(input())          # 첫번째 리스트 입력

# for _ in range(N-1):
#     compare = list(input())     # 비교할 리스트 입력
#     for i in range(len(target)):
#         if target[i] == compare[i]:
#             pass
#         else:       # 다른 글자이면 ?로 변환
#             target[i] = '?'
# print(''.join(target))



N = int(input())
words = []
for _ in range(N):
    word = list(input())
    words.append(word)

compare = words[-1]     # 맨 마지막 input을 비교대상으로 설정

for i in range(N-1):    # 맨 마지막 input을 제외하고 순회
    for j in range(len(words[i])):
        if words[i][j] != compare[j]:
            compare[j] = '?'

print(''.join(compare))







