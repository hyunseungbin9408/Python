# import re
# result = 0
# st = re.compile('[0-9]+')
# calculation_int = []
# calculation_str = []
# for j,i in enumerate(dartResult):
#     str = st.match(i)
#     if str != None:
#         # if i != '0':
#         if i == '1' and dartResult[j+1] == '0':
#             calculation_int.append(int('10'))
#         else:
#             calculation_int.append(int(i))
#     elif i == 'S':
#         calculation_str.append('**1')
#     elif i == 'D':
#         calculation_str.append('**2')
#     elif i == 'T':
#         calculation_str.append('**3')
# print(calculation_int)
# for i,j in enumerate(calculation_str):
#     calculation_int[i] = calculation_int[i] ** int(j[2])
# print(calculation_int)
# print(calculation_str)
# for j, i in enumerate(dartResult):
#     str = st.match(i)
#     if i == '*':
#         for i, k in enumerate(calculation_int):
#             if i == 0 and (k == (int(dartResult[j - 2]) ** int(calculation_str[i][2]))):
#                 calculation_int[i] = calculation_int[i] * 2
#                 if i != 0:
#                     calculation_int[i - 1] = calculation_int[i - 1] * 2
#                     print(calculation_int[i - 1])
#             if i != 0 and (k == (int(dartResult[j - 2]) ** int(calculation_str[i][2]))):
#                 calculation_int[i] = calculation_int[i] * 2
#
#     if i == '#':
#         for i, k in enumerate(calculation_int):
#             if k == (int(dartResult[j - 2]) ** int(calculation_str[i][2])):
#                 calculation_int[i] = calculation_int[i] * (-1)
# print(calculation_int)
# for i in calculation_int:
#     result += i
# print(result)

import re
st = re.compile('[0-9]+')
dartResult = '1S*2T*3S'
result = 0
number = ""
calculation_score = []
for j,i in enumerate(dartResult):
    if i.isnumeric():
        number += i
    elif i == 'S':
        calculation_score.append(int(number) ** 1)
        number = ""
    elif i == 'D':
        calculation_score.append(int(number) ** 2)
        number = ""
    elif i == 'T':
        calculation_score.append(int(number) ** 3)
        number = ""
    elif i == '*':
        if len(calculation_score) > 1:
            calculation_score[-1] = calculation_score[-1] * 2
            calculation_score[-2] = calculation_score[-2] * 2
        else:
            calculation_score[-1] = calculation_score[-1] * 2
    elif i == '#':
        calculation_score[-1] = calculation_score[-1] * -1

for i in calculation_score:
    result += i
print(result)
