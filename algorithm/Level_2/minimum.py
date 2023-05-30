
A = [1, 4, 2]
B = [5, 4, 4]
A.sort()
answer = 0
B.sort(reverse=True)
for i in range(len(B)):
    answer += A[i]*B[i]
#
# arr_b = []
# answer = 0
# for i in B:
#     arr_a = []
#     for j in A:
#         arr_a.append(j * i)
#     arr_b.append(min(arr_a))
#     for j in A:
#         if j * i == min(arr_a):
#             A.remove(j)
# for i in arr_b:
#     answer += i
print(answer)