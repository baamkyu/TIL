# 병합정렬은 쪼갠 후에 합치면서 정렬
# 쪼개기 : 단위가 1개가 될 때 까지, //2 로 나누어줌
# merge_sort # 쪼개기
# merge # 합치기

arr = [69, 10, 30, 2, 16, 8, 31, 22]
def merge_sort(input_list):  # 쪼개기
    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def merge(left, right): # 붙이기
    result = [0] * (len(left)+len(right))
    l = r = idx = 0

    while l < len(left) and r < len(right):     # 범위 안에서
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    while l < len(left):    # 왼쪽이 남은 경우
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):   # 오른쪽이 남은 경우
        result[idx] = right[r]
        r += 1
        idx += 1
    return result

merge_sort(arr)
print(arr)
print(merge_sort(arr))