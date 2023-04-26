def solution(d, budget):
    j = 0
    d.sort()
    for i in range(0,len(d)):
        if (budget - d[i]) >= 0:
            budget -= d[i]
            j += 1
    return j