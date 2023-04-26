def solution(n):
    num = 0
    result = 0
    num = n ** 0.5

    if int(num) == num:
        result = num + 1
        return (int(result * result))
    else:
        return (-1)

