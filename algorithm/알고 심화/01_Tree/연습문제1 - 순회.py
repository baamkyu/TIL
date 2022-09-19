'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(idx):      # 전위 순회하며 출력하는 기능의 함수
    print(idx, end=' ')

    if left_c[idx] != 0:
        preorder(left_c[idx])

    if right_c[idx] != 0:
        preorder(right_c[idx])


E = int(input())    # 정점의 수
E_lst = list(map(int, input().split()))     # 부모-자식 입력

left_c = [0] * (E+1)    # 왼쪽 자식들을 담을 리스트 (인덱스 번호 : 연결된 부모 번호)
right_c = [0] * (E+1)   # 오른쪽 자식들을 담을 리스트 (인덱스 번호 : 연결된 부모 번호)

for i in range(E-1):
    if left_c[E_lst[i*2]] == 0:    # 왼쪽 자식 값이 없다면
        left_c[E_lst[i*2]] = E_lst[i*2+1]
    else:                           # 이미 왼쪽 자식에 값이 있다면
        right_c[E_lst[i*2]] = E_lst[i*2+1]

preorder(1)