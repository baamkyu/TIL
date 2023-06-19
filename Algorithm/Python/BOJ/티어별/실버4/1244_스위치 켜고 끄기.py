# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다.
# ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다. ex) 3 -> 3, 6 변경
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
# 여학생이 3을 받았다면, 3번 스위치를 중심으로 2번, 4번 스위치의 상태가 같고 1번, 5번 스위치의 상태가 같으므로, 1번부터 5번까지 스위치의 상태를 모두 바꾼다.
# 여학생이 4를 받았다면, 3번, 5번 스위치의 상태가 서로 다르므로 4번 스위치의 상태만 바꾼다.

# 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 
# 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다.
# 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다. 
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 남자: 1, 여자: 2


# 스위치 변경 함수
def switch_turn(idx):
   if switch[idx] == 0:
      switch[idx] = 1
   else:
      switch[idx] = 0


switch_num = int(input())      # 스위치의 개수
switch = list(map(int, input().split()))  # 스위치의 상태
student = int(input())  # 학생 수
for _ in range(student):  
    gender, num = map(int, input().split())

    if gender == 1:     # 남자인 경우
      # 배수는 스위치 변경
      for i in range(1, switch_num+1):
         if i % num == 0:
            switch_turn(i - 1)

    elif gender == 2:   # 여자인 경우
      idx = num - 1
      # 입력받은 번호 스위치 변경
      switch_turn(idx)
      
      # 양옆으로 뻗어나갈 수 있는 경우
      i = 1
      while num - i >= 1 and num + i <= switch_num:
         # 양옆이 같으면 모두 스위치 변경
         if switch[idx - i] == switch[idx + i]:
            switch_turn(idx + i)
            switch_turn(idx - i)
        # 양옆이 같지 않으면 중단
         else:
            break
         i += 1

for i in range(switch_num):
   print(switch[i], end = ' ')
   if (i + 1) % 20 == 0:  # 19, 39 ... 일 때 줄바꿈하기
      print()