def solution(n):
    def isprime(n):
        import math
        for check_minor in range(2, int(math.sqrt(n) + 1)):
            if n % check_minor == 0:
                return 0
        else:
            return 1
    j = 0
    for i in range(2,n+1):
        if isprime(i) == 1:
            j += 1
    return(j)