brown = 8
yellow = 1
square = brown + yellow
# def isprime(n):
#     import math
#     for check_minor in range(2, int(math.sqrt(n) + 1)):
#         if n % check_minor == 0:
#             return 0
#     else:
#         return 1
#
# check = 0
# arr_Tran = []
# arr_len = []
# answer = []

# if isprime(square) == 0:
#     for i in range(1, square // 2):
#         if i * i == square:
#             arr_Tran.append(i)
#             arr_len.append(i)
#             break
#     for i in range(3, brown):
#         for j in range(3, brown):
#             if i * j == square and j > i:
#                 arr_Tran.append(j)
#                 arr_len.append(i)
#                 break
#
#     answer.append(min(arr_Tran))
#     answer.append(max(arr_len))
# print(answer)

for i in range(1, square+1):
    if (square//i) == i:
        print(i, i)
        break
    else:
        if (square//i) % 1 == 0:
            j = (square//i)
            if j > i:
                if ((j * 2) + (i*2) == brown + 4) and j * i == square:
                    print(j, i)



