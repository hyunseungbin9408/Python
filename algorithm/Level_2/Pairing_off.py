s = 'baabaabcssxas'
stack = []
for i in range(0, len(s)):
    print(s[i],stack)
    if stack == []:
        stack.append(s[i])
    elif stack[-1] == s[i]:
        stack.pop()
    else:
        stack.append(s[i])
print(stack)


# def check_str(s):
#     if len(s) > 1 and s[0] == s[1]:
#         return 1

# while j < len(check):
#     if check_str(check[j:j+2]) == 1:
#         check.remove(check[j])
#         check.remove(check[j])
#         j = 0
#         k += 2
#     else:
#         j = j + 1
# if k == len(s):
#     print(1)
# else:
#     print(0)
# for i in range(1,len(s)):
#     print(s[i],check[i-1])
#     if s[i] == check[i-1]:
#         check_num = 1
#
# if check_num == 0:
#     print(0)
# else:
#     while j < len(check):
#         print(check)
#         if j+1 >= len(check):
#             break
#         else:
#             print(j,len(check))
#             if check[j] == check[j+1]:
#                 check.remove(check[j])
#                 check.remove(check[j])
#                 j = 0
#             else:
#                 j = j + 1
#     if check == []:
#         print(1)
#     else:
#         print(0)

