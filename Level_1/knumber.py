def solution(array, commands):
    arr_command = []
    arr_result = []
    answer = []
    for i in commands:
        sort_str = sorted(array[i[0] - 1:i[1]:])
        arr_result.append(sort_str)
        arr_command.append(i[2])

    for j,k in enumerate(arr_command):
        answer.append(arr_result[j][k-1])
    return answer