def solution(s):
    import re

    low = re.compile('[a-z]+')
    up = re.compile('[A-Z]+')
    result_low = low.search(s)
    result_up = up.search(s)
    if len(s) == 4 or len(s) == 6:
        if result_up == None and result_low == None:
            return(bool(1))
        else:
            return(bool(0))
    else:
        return(bool(0))