'''
왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과
N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
3
6
8
15
'''

def inorder(n):     # 중위 순회
    global num
    if n:
        inorder(left[n])
        tmp[num][0] = n
        num += 1
        inorder(right[n])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tmp = [[0, i] for i in range(N+1)]    # 순회 담아줄 리스트
    num = 1     # ※ tmp[0] 은 0이기 때문에 1부터 시작해줘야함

    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N//2+1):  # 노드의 개수만큼 (왼쪽 반, 오른쪽 반)
        left[i] = i*2           # 왼쪽 노드 표현
        right[i] = i*2 + 1      # 오른쪽 노드 표현
        if left[i] > N:         # 만약 노드의 값이 노드의 개수보다 커지면 0으로 초기화
            left[i] = 0
        if right[i] > N:        # 만약 노드의 값이 노드의 개수보다 커지면 0으로 초기화
            right[i] = 0
    # print(left)
    # print(right)
    inorder(1)
    tmp.sort()
    # print(tmp)          # sort의 특성 : 첫번째 값을 기준으로 정렬해줌!!
    # print(tmp[1][1])    # 루트값
    # print(tmp[N//2][1])

    # 정답 출력
    print(f'#{tc} {tmp[1][1]} {tmp[N//2][1]}')
