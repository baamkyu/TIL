# 재귀 순열
arr = ['A', 'B', 'C']   # 재료 리스트
sel = [0, 0, 0]         # 인형뽑기 selection
check = [0, 0, 0]       # 뽑을지 말지 결정하는 리스트


def perm(depth):    # 각자 뎁스에서는? 꿈안의 꿈(인셉션)-- ㅡ
    if depth == 3:  # 최고 뎁스에 도달했으면?
        print(sel)  # print
        return
    for i in range(3):              # 3번의 화살표 떨어트릴 기회
        if not check[i]:            # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1            # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = arr[i]     # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0            # 돌아나오면서 다시 다음을 위해 초기화!! (중요)

print(perm(0))



# 중복 순열
arr = ['A', 'B', 'C']
sel = [0, 0, 0]

def perm_rep(depth):
    if depth == 3:
        print(*sel)
        return

    for i in range(3):
        sel[depth] = arr[i]
        perm_rep(depth+1)


print(perm_rep(0))


# 4P2
N = 4
arr = ['a', 'b', 'c', 'd']
sel = [0] * 2
check = [0] * 4


def perm(depth):
    if depth == 2:
