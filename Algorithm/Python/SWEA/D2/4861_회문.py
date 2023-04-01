T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    reverse_matrix = list(zip(*matrix))
    # 회문의 길이가 짝수일 때
    if M % 2 == 0:
        for i in range(N):
            for j in range(N-M+1):
                if matrix[i][j:j+M//2] == matrix[i][j+M//2:j+M][::-1]:
                    answer = matrix[i][j:j+M]
                    break
                elif reverse_matrix[i][j:j+M//2] == reverse_matrix[i][j+M//2:j+M][::-1]:
                    answer = reverse_matrix[i][j:j+M]
                    break
    if M % 2 == 1:
        for i in range(N):
            for j in range(N-M+1):
                if matrix[i][j:j+M//2] == matrix[i][j+M//2+1:j+M][::-1]:
                    answer = matrix[i][j:j+M]
                    break
                elif reverse_matrix[i][j:j+M//2] == reverse_matrix[i][j+M//2+1:j+M][::-1]:
                    answer = reverse_matrix[i][j:j+M]
                    break
    answer = ''.join(answer)
    print(f'#{tc} {answer}')