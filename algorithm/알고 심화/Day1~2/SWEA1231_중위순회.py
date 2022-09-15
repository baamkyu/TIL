def inorder(n):     # 중위 순회
    if n:
        inorder(ch1[n])
        print(n, end = ' ')    # visit(n)
        inorder(ch2[n])

def find_root(V):   # 시작 노드(루트) 찾기
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면
            return i

V = int(input())            # 정점 개수, 마지막 정점 번호
arr = list(input().split())
E = V - 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V + 1)
ch2 = [0]*(V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 자식1로 저장
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)
print('중위순회 : ', end = '')
inorder(root)    # 중위 순회
print()