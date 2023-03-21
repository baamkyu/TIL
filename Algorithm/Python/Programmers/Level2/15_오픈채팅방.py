def solution(record):
    answer = []
    userDB = dict()
    actions = [] # "Enter", "Leave", "Change"
    
    for event in record:
        info = event.split() # action uid [nickname]
        action, userid = info[0], info[1]
        if action in ("Enter", "Change"):
            nickname = info[2]
            userDB[userid] = nickname
        actions.append((action, userid))
        
    for actionInfo in actions:
        action, userid = actionInfo[0], actionInfo[1]
        if action == 'Enter':
            answer.append(f'{userDB[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{userDB[userid]}님이 나갔습니다.')
    
    return answer