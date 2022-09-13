T = int(input())
for tc in range(1, T+1):
    s = input()
    list_s = list(s)    # 인덱싱 사용하기 위해 리스트로 형변환 시켜줌
    for j in range(len(list_s)):                # 문자열(혹은 리스트)의 길이만큼 반복
        try:                                    # 삭제됐을 때 out of range를 방지하기 위함
            for i in range(len(s)):
                if list_s[i] == list_s[i+1]:    # 연속된 두 요소가 같으면
                    del list_s[i]               # 두 요소 모두 삭제해준다
                    del list_s[i]
        except:
            pass
    print(f'#{tc} {len(list_s)}')