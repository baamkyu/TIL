'''
2
0DEC
0269FAC9A0
'''

T = int(input())
dic = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
       '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

for tc in range(1, T+1):
    bit = input()
    temp = bin(int(bit, 16))[2:]   # 16진수 -> 2진수로 변환
    ans = '0'*(len(bit)*4 - len(temp)) + temp   # 사용할 2진수 비트

    idx = ans[::-1].index('1')      # 뒤에 1이 나올 때까지의 인덱스를 구해줌
    ans = ans[:-idx]               # 인덱스를 구한 만큼 뒤에 잘라줌

    real_ans = []
    for i in range(len(ans), -1, -6):   # 뒤에서부터 6개씩 찾아줌
        if ans[i-6:i] in dic:           # dic안에 있는 것들만 출력
            real_ans.append(dic[ans[i-6:i]])
    print(*real_ans[::-1])