def solution(lottos, win_nums):
    lottos_rank = (6,6,5,4,3,2,1)

    answer = []
    j = 0
    result = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            j += 1
    answer = [lottos_rank[result+j],lottos_rank[j]]


    return answer