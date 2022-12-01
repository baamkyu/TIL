import sys
sys.stdin = open('input_4835.txt')

T = int(input())                        # 테스트케이스의 수
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N=정수의 개수, M=구간의 개수
    data = list(map(int, input().split()))
    data_max = 1                        # 임의의 최대값 설정
    data_min = 10000*M                  # 임의의 최소값 설정
    data_hap = []                       # 연속된 인덱스들의 합 리스트
    for i in range(N-M+1):              # out of index 되지 않도록 범위를 N-M+1까지 설정
        data_hap2 = 0
        for k in range(i, i+M):         # data_hap에 데이터들의 합 추가하기
            data_hap2 += data[k]
        data_hap.append(data_hap2)

        if data_max < data_hap[i]:      # data_hap 리스트 속에서 최대값을 data_max에 할당
            data_max = data_hap[i]
        if data_min > data_hap[i]:      # data_hap 리스트 속에서 최소값을 data_min에 할당
            data_min = data_hap[i]
        max_min_diff = data_max - data_min
    print(f'#{tc} {max_min_diff}')
