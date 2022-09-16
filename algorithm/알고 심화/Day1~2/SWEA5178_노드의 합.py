'''
1
5 3 2
4 1
5 2
3 3
'''

T = int(input())
for tc in range(1, T+1):
    # N : 노드의 개수, M : 리프 노드의 개수, L : 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    tree = [0] * (N+1) + [0]

    leaf_lst = []
    num_lst = []
    for _ in range(M):  # 노드 번호와 값을 리스트로 받아줌
        leaf, num = map(int, input().split())
        leaf_lst.append(leaf)
        num_lst.append(num)

    for i in leaf_lst:  # 노드 번호와 일치하는 곳에 값을 넣어줌
        tree[i] = num_lst.pop(0)

    for i in range(len(tree)//2-1, 0, -1):
        if tree[i] == 0:
            tree[i] = tree[i*2] + tree[(i*2)+1]

    print(f'#{tc} {tree[L]}')