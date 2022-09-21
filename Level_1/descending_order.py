def solution(n):
    len_str = len(str(n))
    answer = str(n)
    result = []
    result_value = ""

    for i in range(len_str - 1, 0, -1):
        result.append(int(answer[i]))
    result.append(int(answer[0]))
    result_list = reversed(sorted(result))

    for i in list(result_list):
        result_value += str(i)
    return (int(result_value))