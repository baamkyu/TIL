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
    global cnt
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

    if left[-1] > right[-1]:
        cnt += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort_arr = merge_sort(arr)
    print(f'#{tc} {merge_sort_arr[N//2]} {cnt}')