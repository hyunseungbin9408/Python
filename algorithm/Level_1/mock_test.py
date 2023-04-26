arr = [1,2,3,4,5]
give_one = [1,2,3,4,5]

give_two = [2, 1, 2, 3, 2, 4, 2, 5]

give_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answer_count = [0,0,0]
answer_result = []
for i,value in enumerate(arr):

    if value == give_one[i%len(give_one)]:
        answer_count[0] += 1
    if value == give_two[i%len(give_two)]:
        answer_count[1] += 1
    if value == give_three[i%len(give_three)]:
        answer_count[2] += 1

for index,k in enumerate(answer_count):
    if k == max(answer_count):
        answer_result.append(index+1)
print(answer_result)
# if one_count>=1 and two_count>=1 and three_count>=1:
#     if (one_count == two_count == three_count):
#         print([1,2,3])
#     elif(two_count == three_count):
#         print([2, 3])
#     elif(one_count == two_count):
#         print([1, 2])
#     elif(one_count == three_count):
#         print([1,3])
# else:
#     result_arr =[]
#     if max(one_count,two_count,three_count) == one_count:
#         print([1])
#     elif max(one_count,two_count,three_count) == two_count:
#         print([2])
#     elif max(one_count,two_count,three_count) == three_count:
#         print([3])