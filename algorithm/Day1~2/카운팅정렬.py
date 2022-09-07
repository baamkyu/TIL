# 카운팅정렬 : 항목들의 순서를 결정하기 위해 집합의 각 항목이 몇 개씩 있는지 세는 작업
# <정렬 과정>
# count하기 위한 빈 리스트 생성

lst = [0, 4, 1, 3, 1, 2, 4, 1]
max_lst = max(lst)
count_lst = [0]*(max_lst+1)
for i in lst:
    count_lst[i] += 1
print(count_lst)