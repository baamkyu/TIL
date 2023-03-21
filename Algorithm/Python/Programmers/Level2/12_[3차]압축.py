D = {chr(i) : i-64 for i in range(65,91)} # 사전

def solution(msg):
    answer = []
    msg = list(msg) + ["0"]
    idx = 27 # 사전 색인 번호
    start, end = 0, 1 # 단어 인덱스 시작, 끝
    while end < len(msg):
        # 사전에 없는 단어가 나올때까지 단어 인덱스 + 1
        while ''.join(msg[start:end]) in D:
            end += 1
            
        # 새로운 단어 사전에 추가
        D[''.join(msg[start:end])] = idx
        idx += 1
        
        # 현재 단어 색인 번호 출력
        answer.append(D[''.join(msg[start:end-1])])
        
        # 단어 인덱스 갱신
        start, end = end - 1, end
        
    return answer