# 문자열을 2진법으로 변환 -> 7개씩 나눔 -> 10진법으로 변환
'''
2
0F97A3
01D06079861D79F99F
'''

T = int(input())
for tc in range(1, T+1):
    bit = input()
    temp = bin(int(bit, 16))[2:]    # 16진법을 10진법으로 => int(bit, 16)
                                    # 10진법을 2진법으로 => bin(__)
                                    # [2:] 해준 이유는 앞 2자리에 '0b' 나오는 것을 잘라주기 위해

    ans = '0'*(len(bit)*4 - len(temp)) + temp   # 16진수의 비트 수와 2진수의 비트 수와 맞춰주기 위해

    for i in range(0, len(ans), 7):
        print(int(ans[i:i+7], 2), end = ' ')
    print()