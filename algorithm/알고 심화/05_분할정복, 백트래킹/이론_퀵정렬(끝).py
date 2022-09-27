a = [2, 8, 7, 1, 3, 5, 6, 4]

# left, right는 값을 지정하는 변수
# low, high는 인덱스를 지정하는 변수

def lomuto(low, high):
    def partition(low, high):   # 칸막이의 위치를 뱉고, 피봇 기준으로 앞/뒤 정렬을 하는 함수
        pivot = a[high]  # 임의로 마지막 값을 pivot 설정
        left = low       #

        for right in range(low, high):
            if a[right] < pivot:
                a[left], a[right] = a[right], a[left]
                left += 1
        a[left], a[high] = a[high], a[left]

        return left

    if low < high:  # 적어도 리스트 길이가 2 이상이어야 함.
        pivot = partition(low, high)
        lomuto(low, pivot - 1)
        lomuto(pivot + 1, high)

lomuto(0, len(a)-1)
print(a)