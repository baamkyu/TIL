# 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬하시오.
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
N = int(input())
words = set()
for _ in range(N):
    words.add(input())

# 빈 리스트에 정렬하기 위해 [단어의 길이, 단어] 형태로 담아줌
tmp = []
for word in words:
    tmp.append([len(word), word])
sort_lst = sorted(tmp)

# 출력
for len, word in sort_lst:
    print(word)