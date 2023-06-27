# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하라.
T = int(input())
for _ in range(T):
    sen = list(input().split())
    for i in range(len(sen)):
        sen[i] = sen[i][::-1]
    print(' '.join(sen))