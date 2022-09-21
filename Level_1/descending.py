def solution(s):
    arr_low = []
    arr_up = []
    result = ""
    for i in s:
        if i.islower():
            arr_low.append(i)
        else:
            arr_up.append(i)
    arr_low.sort(reverse=True)
    arr_up.sort(reverse=True)
    for j in arr_low:
        result += j
    for k in arr_up:
        result += k
    return result