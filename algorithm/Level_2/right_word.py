s = "(()("

# arr =[]
# if len(s) <= 1:
#     print(False)
# else:
#     for i in s:
#         if i == '(':
#             arr.append(i)
#         else:
#             if len(arr) == 0:
#                 print(False)
#             else:
#                 arr.remove(arr[-1])
#
#     print(arr)
#     if len(arr) != 1:
#         print(True)

def solution(s):
    arr = []
    if len(s) <= 1:
        return (False)
    else:
        for i in s:
            if i == '(':
                arr.append(i)
            else:
                if len(arr) == 0:
                    return (False)
                    break
                else:
                    arr.pop(-1)
        if len(arr) != 0:
            return (False)
        else:
            return (True)


