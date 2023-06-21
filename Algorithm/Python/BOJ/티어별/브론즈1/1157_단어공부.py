# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

word = input().upper()
word_li = list(set(word))
cnt = []
for i in word_li:
    i_cnt = word.count(i)
    cnt.append(i_cnt)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_li[cnt.index(max(cnt))])