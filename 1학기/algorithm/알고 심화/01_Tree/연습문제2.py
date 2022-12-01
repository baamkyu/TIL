'''
4
1 2 1 3 3 4 3 5
'''

def find_root(V):   # 시작 노드(루트) 찾기
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면
            return i

def f(n):       # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
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
print(f(root))
print(f(3))