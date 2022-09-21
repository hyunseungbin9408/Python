def solution(n):
    to_list = []

    to_str = str(n)
    for i in to_str:
        to_list.append(int(i))

    return(list(reversed(to_list)))