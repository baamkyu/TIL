#  이곳에 코드와 주석을 작성합니다.
T = int(input())


def constructible(runway):  # 경사로 건설이 제대로 이루어져 하나의 runway 가 정상작동 할 수 있나? 검증하는 함수
    verification = True  # 기본값은 True 인데 조건에 안걸리면 False 로 바꾸고 break 거는 식으로 구조화
    slopes = [0]*N  # 경사로가 어디 설치돼있는지 확인하기 위한 배열

    for j in range(N-1):  # 하나의 활주로에 대해 순회하면서 자기와 오른쪽을 비교!
        if abs(runway[j] - runway[j+1]) > 1:  # 애초에 바로 옆과 높낮이가 2 이상 나면 경사로고 뭐고 없음 걍 건설불가
            verification = False
            break
        elif runway[j] == runway[j+1]:  # 둘이 높이가 같다면 넘어감
            continue
        elif runway[j] - runway[j+1] == 1:  # 왼쪽이 1 높은 경우, '맵안에서' 오른쪽 방향으로 경사로를 건설해야함
            # 경사로를 따질땐 2가지를 살펴봐야함 -> 경사로 건설을 위해 오른쪽으로 x만큼 보는데 맵밖으로 벗어나지 않을것!
            # 그리고 맵 안이더라도 오른쪽 방향인데 계단위에 건설하면 안되니까 오른쪽 방향 x 만큼까지의 높이가 모두 동일할것! set 처리 응용해서 보자
            # 인덱스 슬라이싱에서는 j+M 이 미만으로 들어갈거여서 여기 부등호 조심해줘야함 -> j+X = N-1 까지는 괜찮음 -> 단축평가 중요함!!
            # if 순서대로 맵 안인가? 평평한가? 경사로가 건설돼있는가? 를 검증함. 하나라도 망하면 break 걸도록
            if j+X > N-1 or len(set(runway[j+1:j+X+1])) != 1 or sum(slopes[j+1:j+X+1]) > 0:  # 경사로 건설돼있는지 확인
                verification = False
                break
            else:  # 슬라이싱 연산으로 넣기 -> 경사로를 설치합니다.
                slopes[j+1:j+X+1] = [1]*X

        elif runway[j] - runway[j+1] == -1:  # 오른쪽이 1 높은 경우, 왼쪽 방향으로 경사로를 건설해야함
            if j-X+1 < 0 or len(set(runway[j-X+1:j+1])) != 1 or sum(slopes[j-X+1:j+1]) > 0:
                verification = False
                break
            else:
                slopes[j-X+1:j+1] = [1]*X


    return verification

for tc in range(1, T+1):
    N, X = map(int, input().split())  # N 한변길이, X = 경사로 길이
    runways = [list(map(int, input().split())) for _ in range(N)]  # 전체정보
    transposed_runways = list(zip(*runways))  # 전치 행렬
    answer = 0

    for i in range(N):  # 가로 세로 한행씩 보게 됨.
        if constructible(runways[i]):
            answer += 1
        if constructible(transposed_runways[i]):
            answer += 1

    print('#{} {}'.format(tc, answer))


# T = int(input())
# for tc in range(1, T+1):
#     N, X = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 경사로의 길이 X는 2이상 4이하의 정수
#
#     # 가로 탐색
#     for k in range(N):
#         board = arr[k]
#         pre = board[0]
#         i = 1
#         while i < N:
#             if pre == board[i]:     # 같은 값이 연속되면 + 1
#                 cnt += 1
#             else:
#                 if pre + 1 == board[i]: # 오르막
#                     if cnt < X:
#                         break
#                     elif cnt >= X:
#                         cnt = 1
#                         pre += 1
#                 elif pre - 1 == board[i]:   # 내리막
#                     for j in range(N-i):
#                         if
#                     if cnt < X:
#
#                 else:
#                     break