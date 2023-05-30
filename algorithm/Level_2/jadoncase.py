def solution(s):
    s = s.lower()
    string = s.split(" ")
    result = ""
    for i,j in enumerate(string):
        if i != len(string)-1:
            result += j.capitalize() + ' '
        else:
            result += j.capitalize()
    return result