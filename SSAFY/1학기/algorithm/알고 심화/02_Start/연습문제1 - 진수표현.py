'''
2
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111
'''

T = int(input())
for tc in range(1, T+1):
    bit = input()
    for i in range(0, len(bit), 7):
        print(int(bit[i:i+7], 2), end = ' ')
    print()