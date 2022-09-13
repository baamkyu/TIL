# # 재귀 순열
# arr = ['A', 'B', 'C']   # 재료 리스트
# sel = [0, 0, 0]         # 인형뽑기 selection
# check = [0, 0, 0]       # 뽑을지 말지 결정하는 리스트
#
#
# def perm(depth):    # 각자 뎁스에서는? 꿈안의 꿈(인셉션)-- ㅡ
#     if depth == 3:  # 최고 뎁스에 도달했으면?
#         print(sel)  # print
#         return
#     for i in range(3):              # 3번의 화살표 떨어트릴 기회
#         if not check[i]:            # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
#             check[i] = 1            # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
#             sel[depth] = arr[i]     # 화살표가 떨어진 위치의 재료리스트
#             perm(depth+1)
#             check[i] = 0            # 돌아나오면서 다시 다음을 위해 초기화!! (중요)
#
# print(perm(0))

arr = ['A', 'B', 'C']  # 재료 리스트
sel = [0, 0, 0]  # 인형뽑기 selection
check = [0, 0, 0]  # 뽑을지 말지 결정하는 리스트


def perm(depth):    # depth는 sel의 idx
    if depth == 3:  # 알파벳을 다 채우고 idx를 초과 했으면,
        print(sel)  # print
        return      # break

    for i in range(3):  # 0 -> A, 1 -> B, 2 -> C
        if not check[i]:  # A, B, C가 사용 되었는지 체크
            check[i] = 1  # 사용하지 않은 알파벳을 사용한다 check
            sel[depth] = arr[i]  # 뎁스 = idx, i(알파벳)을 넣는다.
            perm(depth+1)   #sel의 다음 인덱스로 이동.
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)
                        #주의! 아직 포문 안끝남. 다음 포문 진행.

perm(0)
# depth 0, range 0(A) A00 -> depth 1, range 0(A) 존재 pass -> depth 1, range 1(B) -> AB0
#-> ABC -> depth 3 재귀 탈출 -> AB0 depth 2의 range 3 소멸
#-> A00 depth 1 range 1(B)소멸 range 2(C) 시작 -> AC0 -> ACB -> AC0
#-> A00 depth 1 range 2(C)소멸 depth 끝
#-> 000 depth 0 range 1(B) 시작 -> B00


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
