def solution(arr):
    arr_result = []
    arr_result.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            arr_result.append(arr[i])
    return arr_result
