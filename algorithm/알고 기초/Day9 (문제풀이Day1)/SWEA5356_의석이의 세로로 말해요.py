import sys
sys.stdin = open('SWEA5356_의석이의 세로로 말해요.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    word = [input() for _ in range(5)]
    print(f'#{tc} ', end = '')
    for i in range(15):
        for j in range(5):
            print(word[j][i:i+1], end = '')
    print('')