S = input()  # @===@==@=@==(^0^)==@=@===@
count_left = 0
count_right = 0
center = 0

for i in range(len(S)):  # 0을 center 로 잡음
    if S[i] == "0":
        center = i

for i in range(len(S)-1):
    if i < center and S[i] == "@" and S[i+1]== "=": # 0보다 왼쪽에 있는 경우
        count_left += 1
    elif i > center and S[i]== "=" and S[i+1] == "@":  # 0보다 오른쪽에 있을 때 @
        count_right += 1

print(count_left, count_right)




















