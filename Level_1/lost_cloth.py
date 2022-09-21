n = 5
lost = [2,4]
reserve	= [1, 3, 5]
arr = []

# for i in range(1, n+1):
#     arr.append(i)
#
# lost_index = []
# reserve_index = []
# for j,k in enumerate(arr):
#     if k in lost:
#         lost_index.append(j)
#     if k in reserve:
#         reserve_index.append(j)
#
# fill_count = 0
# if len(lost) != 0 and len(reserve) != 0:
#     if lost[-1]-1 in reserve:
#         if len(reserve) >= len(lost):
#             for i in range(len(lost)):
#                 if arr[lost_index[i]-1] in reserve or arr[lost_index[i]+1] in reserve:
#                     fill_count += 1
#         else:
#             for i in range(len(reserve)):
#                 if arr[lost_index[i]-1] in reserve or arr[lost_index[i]+1] in reserve:
#                     fill_count += 1
#
# answer = n - len(lost) + fill_count
# print(answer)

set_reserve = set(reserve) - set(lost)
set_lost = set(lost) - set(reserve)

for i in set_reserve:
    if i-1 in set_lost:
        set_lost.remove(i-1)
    elif i + 1 in set_lost:
        set_lost.remove(i + 1)
print(set_lost)
answer = n - len(set_lost)