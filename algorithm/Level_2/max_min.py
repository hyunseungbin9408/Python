def solution(s):
    string = s.split(" ")
    result = []
    answer = ""
    for i in string:
        result.append(int(i))
    answer = f"{min(result)} {max(result)}"
    return answer