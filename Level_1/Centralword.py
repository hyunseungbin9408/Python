def solution(s):
    s_len = len(s)
    s_digit = s_len / 2
    if s_len % 2 != 0:
        if (int(s_digit) * 2) + 1 == s_len:
            j = int(s_digit)
            return(s[j])
    else:
        if (int(s_digit) * 2) == s_len:
            j = int(s_digit)
            return(s[j-1:j+1])