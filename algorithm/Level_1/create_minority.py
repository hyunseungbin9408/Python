def solution(nums):
    def isprime(n):
        import math
        for check_minor in range(2, int(math.sqrt(n) + 1)):
            if n % check_minor == 0:
                return 0
        else:
            return 1

    from itertools import combinations
    nums_list = list(combinations(nums,3))
    j = 0
    for i in nums_list:
        if isprime(sum(i)) == 1:
            j += 1
    return(j)
