# 다섯개의 단어를 입력받고 이를 세로로 읽어라.
words = []
for _ in range(5):
    word = list(map(str, input()))
    words.append(word)

col = ''
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            col += words[j][i]
print(col)