input = str(input())

face_index = 0
left = 0
right = 0
for i in range(len(input)):
    if input[i:i+5] == '(^0^)':
        face_index = i
for l in range(face_index):
    if input[l] == '@' and input[l+1] == '=':
        left += 1
for r in range(face_index+5, len(input)):
    if input[r] == '=' and input[r+1] == '@':
        right += 1
print(left, right)