def solution(num):
    answer = 0
    while num != 1:
        if num % 2 != 0:
            num = (num * 3) + 1
        else:
            num = num / 2
        answer = answer + 1
    if answer > 501:
        return(-1)
    else:
        return(answer)

#return answer