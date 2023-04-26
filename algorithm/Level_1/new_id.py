new_id = ".z-+.^."
new_id2 = "...!@BaT#*..y.abcdefghijklm"
# if new_id == '':
#     new_id = 'a'
# else:
#     new_id = new_id.lower()
# arr = []
# result = []
# import re
# p = re.compile('[a-z0-9]|[.]|[_]|[-]|[\s]')
# for i in range(len(new_id)):
#     check = p.match(new_id[i])
#     if check != None:
#         arr.append(new_id[i])
# print(arr)
# print(result)
# for i,j in enumerate(arr):
#     if i > 1:
#         if arr[i] == '.':
#             if arr[i-1] != '.':
#                 result.append(j)
#         else:
#             result.append(j)
#     else:
#         result.append(j)
# if len(result) == 0:
#     result.append('a')
# for i in result:
#     if result[0] == '.':
#         result.remove(result[0])
# if len(result) == 0:
#     result.append('a')
# if result[-1] == '.':
#     result.pop(-1)
# if len(result) > 15:
#     result = result[:15]
# if result[-1] == '.':
#     result.pop(-1)
# if len(result) < 3:
#     while len(result) <= 2:
#         result.append(result[-1])
# answer = ''
# for i in result:
#     answer += i
# print(answer)

def solution(new_id):
    import re
    if new_id == '':
        new_id = 'a'
    answer = new_id.lower()#|[.]|[_]|[-]
    answer = re.sub('[^a-z0-9-_.]','',answer)
    answer = re.sub('\.+','.',answer)
    answer = re.sub('^[.]|[.]$','',answer)
    answer = answer[:15]
    answer = re.sub('^[.]|[.]$','',answer)
    if answer == '':
        answer = 'a'
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    return answer