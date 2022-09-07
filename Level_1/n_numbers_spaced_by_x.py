x=-4
n=5
answer = []

# if (x >= -10000000)and(x<=10000000)and(n<=1000)and(n>0):
#     for j in range(1, n+1):
#         answer.append(x * j)
#
#     if answer[0] > 0:
#         answer_value = sorted(list(set(answer)))
#     else:
#         answer_value = sorted(list(set(answer)),reverse = True)
#     print(answer_value)

test = [x * i for i in range(1, n + 1)]
print(test)