def solution(n):
    answer, num = 0, 1
    for i in range(0, n):
        answer, num = num, answer + num

    return (answer % 1234567)