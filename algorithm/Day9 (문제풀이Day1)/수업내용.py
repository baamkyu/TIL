# # 재귀함수로 부분집합 구하기
#
# arr = ['A', 'B', 'C']  # 재료 리스트
# check = [0, 0, 0]  # 위치 체크용 리스트
#
# def powerset(idx):  # 재귀 깊이가 파라미터
#     if idx == 3:   # 마지막 깊이에 도달했다면?
#         print('체크 배열은 다음과 같음: ', *check)  # 이 당시의 check 배열 현황
#         result = []
#         for j in range(3):  # 체크 배열을 하나씩 보면서
#             if check[j] == 1:  # 살아있다면?
#                 result.append(arr[j])  # 그 위치를 res에 담음
#         print(result)  # res 프린트!
#         return
#
#     check[idx] = 0
#     powerset(idx + 1)
#
#     check[idx] = 1
#     powerset(idx + 1)
#
#     # for i in range(2):
#     #     check[idx] = i
#     #     powerset(idx+1)
#
# powerset(0)

# # for문 순열
# arr = ['A', 'B', 'C']
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i != j and j != k and k != i:      # 원소가 다 다른 경우 (중복순열은 이거 빼면 됨)
#                 print([arr[i], arr[j], arr[k]])

# 재귀 순열
arr = ['A', 'B', 'C']  # 재료 리스트
sel = [0, 0, 0]  # 인형뽑기 selection
check = [0, 0, 0]  # 뽑을지 말지 결정하는 리스트


def perm(depth):  # 각자 뎁스에서는? 꿈안의 꿈(인셉션)
    if depth == 3:  # 최고 뎁스에 도달했으면?
        print(sel)  # print
        return

    for i in range(3):  # 3번의 화살표 떨어트릴 기회
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = arr[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)


perm(0)