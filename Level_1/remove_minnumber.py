def solution(arr):
    arr_len = len(arr)
    if arr_len != 1:
        min_value = min(arr)
        arr.remove(min_value)
        return arr
    else:
        return [-1]