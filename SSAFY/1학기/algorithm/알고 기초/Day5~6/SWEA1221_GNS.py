T = int(input())  # 테스트케이스 개수 입력
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T + 1):
    text = list(map(str, input().split(" ")))  # 테스트케이스 입력
    new_num_index = []  # 테스트케이스들의 인덱스번호를 넣을 리스트
    for num_index, num_value in enumerate(num):  # 인덱스 번호를
        for i in text:  # 테스트케이스의 요소들
            if i == num_value:  # num_value == 테스트케이스의 요소일 때 인덱스값 출력
                new_num_value.append(num_value)
    print(new_num_value)  # 뜻밖의 정렬이 자동
