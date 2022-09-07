import sys
sys.stdin = open('SWEA5356_의석이의 세로로 말해요.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    S = [list(input()) for _ in range(5)]
    word_lst = []
    len_S = []
    for k in range(len(S)):         # 가장 긴 리스트의 길이를 알기 위함
        len_S.append(len(S[k]))
    max_len_S = max(len_S)

    for j in range(max_len_S):      # 남는 값 없이 입력하기 위해 최대를 range범위로 줌
        for i in range(5):
            try:                    # word_lst.append(S[i][j])를 시도해봐라. 에러나면 pass해라.
                word_lst.append(S[i][j])
            except:
                pass

    word = ''.join(word_lst)
    print(f'#{tc} {word}')