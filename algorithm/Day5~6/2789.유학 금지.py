# 1
word = list(input())
word2 = []
for i in word:
    if i != "C" and i != "A" and i != "M" and i != "B" and i != "R" and i != "I" and i != "D" and i != "G" and i != "E":
        word2.append(i)
print(''.join(word2))

# 2
S = list(input())
new_word = []
warning_word = list(map(str, 'CAMBRIDGE'))
for i in range(len(S)):
    if S[i] not in warning_word:
        new_word.append(S[i])
new_word = ''.join(new_word)
print(new_word)














