# 버블정렬 : 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
# <정렬과정>
# 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 마지막 자리까지 이동한다.
# 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다
lst = [55, 7, 78, 12, 42]
N = len(lst)
for i in range(N-1, 0, -1):     # 첫번째 정렬은 0~N-1 인덱스까지, 다음 정렬은 0~N-2 인덱스까지 반복
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)


lst = [55, 7, 78, 12, 42]
N = len(lst)
for i in range(N-1):  # N이 5이면 4번만 정렬을 하면 된다. (마지막은 자연스래 정렬되기 때문)
    for j in range(N-1):  # 인덱스 번호는 N-1까지 해야 out of index가 안 뜸.
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)





























