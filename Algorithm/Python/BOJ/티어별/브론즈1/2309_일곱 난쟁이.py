# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다.
# 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다.
# 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 진짜 일곱 난쟁이를 찾아라.

height = [int(input()) for _ in range(9)]
height_sum = sum(height)

false_1 = 0 # 가짜 난쟁이 1번
false_2 = 0 # 가짜 난쟁이 2번

# 9명 키의 합에서 두명의 키를 뺐을 때 100이면 그 두명이 가짜난쟁이 1,2번이 된다
for i in range(8):
    for j in range(i+1, 9):
        if height_sum - height[i] - height[j] == 100:
            false_1 = height[i]
            false_2 = height[j]
            break
        
# 가짜 난쟁이 제거
height.remove(false_1)
height.remove(false_2)

# 출력
for i in sorted(height):
    print(i)