stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

result_dic = {}

players = len(stages)
for stage in range(1,N+1):
    if players != 0:
        stage_level = stages.count(stage)
        result_dic[stage] = stage_level / players
        players -= stage_level
    else:
        result_dic[stage] = 0

result_answer = list(sorted(result_dic.items(),key=lambda x: x[1],reverse=True))
result_answer_list = []
for i in result_answer:
    result_answer_list.append(i[0])
print(result_answer_list)

# stages_array = list(sorted(stages))
# Failure_rate = [0] * n
# Failure_playes = [0] * n
# result_dic = {}
# if len(stages_array) != 0:
#     for idx, value in enumerate(stages_array):
#         if len(stages) != 0:
#             if value >= 1:
#                 Failure_rate[0] += 1
#                 if value == 1:
#                     Failure_playes[0] += 1
#             if value >= 2:
#                 Failure_rate[1] += 1
#                 if value == 2:
#                     Failure_playes[1] += 1
#             if value >= 3:
#                 Failure_rate[2] += 1
#                 if value == 3:
#                     Failure_playes[2] += 1
#             if value >= 4:
#                 Failure_rate[3] += 1
#                 if value == 4:
#                     Failure_playes[3] += 1
#             if value >= 5:
#                 Failure_rate[4] += 1
#                 if value == 5:
#                     Failure_playes[4] += 1
#     for idx, value in enumerate(Failure_rate):
#         result_dic[idx+1] = str(Failure_playes[idx]/value)
# else:
#     for idx, value in enumerate(Failure_rate):
#         result_dic[idx+1] = str(0)
#
# result_answer = list(sorted(result_dic.items(),key=lambda x: x[1],reverse=True))
# result_answer_list = []
# for i in result_answer:
#     result_answer_list.append(i[0])
# print(result_answer_list)