'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

def cnt_node(n):
    global cnt
    if n:
        cnt += 1    # 노드에 들어갈 때마다 1씩 더하기
        cnt_node(left[n])   # 왼쪽 자식으로
        cnt_node(right[n])  # 오른쪽 자식으로


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # 간선의 개수 E, N을 서브트리의 루트로 갖는 노드의 수를 구할 것임
    E_lst = list(map(int, input().split()))   # E개의 부모 자식 노드 번호 쌍

    # 노드 번호는 1번부터 E+1번까지 존재
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p = E_lst.pop(0)   # 부모 노드
        c = E_lst.pop(0)   # 자식 노드
        # 왼쪽 자식이 없다면, 왼쪽 자식부터
        if not left[p]:
            left[p] = c
        # 오른쪽 자식이 없다면, 오른쪽 자식으로
        else:
            right[p] = c

    cnt = 0
    cnt_node(N)  # N번 노드부터 시작하는 서브 트리의 노드 개수 구하기

    print(f'#{tc} {cnt}')