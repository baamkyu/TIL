import sys
input = sys.stdin.readline

words = [list(input()) for _ in range(5)]

# 최대 15글자, 5개의 단어
for i in range(15):
    for j in range(5):
        if i < len(words[j]) - 1:   # sys.stdin.readline을 사용하면 \n 까지 입력받게 되어 이걸 제외시켜주려고 -1 했음
            print(words[j][i], end = '')
