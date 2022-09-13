# 조합 2개뽑기 (그냥 조합)
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i+1, 3):     # i가 A일 때, j에 A는 제외하고 들어갈 수 있음.
        print(arr[i], arr[j])   # A B , A C , B C 3개 나옴.



# 중복조합 2개뽑기
print("중복조합 2개 뽑기")
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i, 3):       # i가 A일 때, j에 A도 들어갈 수 있음.
            print(arr[i], arr[j])   # A A, A B, A C, B B, B C, C C


# 3개 뽑으려면 for문 한 줄 더 쓰고 print에 arr[k] 추가해주면 됨



# 재귀 조합 (그냥 조합)
# 5C3
arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]

def combination(idx, sidx):
    if sidx == 3:  # sel 길이 범위를 벗어나면 sel이 확정됐다는 소리니까 print
        print(sel)
        return

    if idx == 5:  # 얘도 벗어나지 않아야 함
        return

    sel[sidx] = arr[idx]  # sidx가 가리키는 위치에 idx가 가리키는 재료를 넣음
    combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
    combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.

combination(0, 0)



# 재귀 중복 조합
def combi_rep(idx, sidx):
    if sidx == m:
        print(*sel)
        return

    if idx == n:
        return

    sel[sidx] = arr[idx]
    combi_rep(idx, sidx+1)
    combi_rep(idx+1, sidx)

n, m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0] * m
combi_rep(0, 0)