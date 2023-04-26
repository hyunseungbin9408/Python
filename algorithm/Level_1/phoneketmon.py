def solution(nums):
    arr = nums
    arr_len = int(len(arr)/2)
    arr_unique = len((list(set(arr))))

    if arr_unique < arr_len:
        return(arr_unique)
    else:
        return(arr_len)