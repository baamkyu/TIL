N = int(input())
input_list = []
for _ in range(N):
    input_list.append(input())

first = input_list[0]

# listnum : 몇번째 리스트 ?
# letternum : 몇번째 글자 ?
for listnum in range(1, N):
    for letternum in range(len(first)):
        if input_list[listnum][letternum] == first[letternum]:
            pass
        elif input_list[listnum][letternum] != first[letternum]:
            first[letternum] = "?"
        