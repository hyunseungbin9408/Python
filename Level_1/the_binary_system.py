def solution(n):
    import string

    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r]
        else :
            return convert(q, base) + tmp[r]

    result = convert(n,3)

    result_arr = []
    for i in str(result):
        result_arr.append(i)
    result = ""
    result_arr.reverse()
    for j in result_arr:
        result += j
    return int(str(result),3)