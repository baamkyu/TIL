import sys
sys.stdin = open('list2_이진탐색.txt', 'r')

T = int(input())
for tc in range(T):
    P, Pa, Pb= list(map(int, input().split()))
    l_a = 1
    r_a = P
    l_b = 1
    r_b = P
    count_a = 1
    count_b = 1
    middle_a = int((P+l_a)/2)
    middle_b = int((P+l_b)/2)
    while middle_a != Pa:
        if middle_a > Pa:
            count_a += 1
            r_a = middle_a
            middle_a = int((l_a + r_a) / 2)
        elif middle_a < Pa:
            count_a += 1
            l_a = middle_a
            middle_a = int((l_a + r_a) / 2)

    while middle_b != Pb:
        if middle_b > Pb:
            count_b += 1
            r_b = middle_b
            middle_b = int((l_b + r_b) / 2)
        elif middle_b < Pb:
            count_b += 1
            l_b = middle_b
            middle_b = int((l_b + r_b) / 2)

    if count_a < count_b:
        print(f'#{tc+1} A')
    elif count_a > count_b:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc+1} 0')