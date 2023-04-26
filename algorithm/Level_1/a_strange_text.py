def solution(s):
    to_result = ""

    for upper in s.split(" "):
        for i in range(len(upper)):
            if i % 2 == 0:
                to_result += upper[i].upper()
            else:
                to_result += upper[i].lower()
        to_result += " "
    return to_result[0:-1]