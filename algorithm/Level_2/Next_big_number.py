def solution(n):
    bin_n = str(bin(n)[2:])
    for i in range(n + 1, 1000001):
        check_one = str(bin(i)[2:])
        if bin_n.count('1') == check_one.count('1'):
            return i
            break
