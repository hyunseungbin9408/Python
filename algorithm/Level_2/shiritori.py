words = ["hello", "one", "even", "never", "now", "world", "draw"]
n = 2
check_arr =[]
check_word = ''
check_value_last = []
check_arr.append(words[:n])
check_value = []
check_number = 0
answer = [0, 0]
for i in range(0, (len(words) // n)):
    #print(list(islice(words, None, n * i)))
    check_value = words[(n * i):(n * i) + n:]
    check_number = i+1
    if i != 0:
        for j in range(len(check_value)):
            if check_word != '':
                print(check_value[j][0], check_word[-1])
                if check_value[j][0] != check_word[-1]:
                    answer = [j + 1, check_number]
            if check_value[j] in check_value_last:
                answer = [j+1,check_number]
            check_word = check_value[j]
    for k in check_value:
        check_value_last.append(k)
    check_arr.append(words[(n*i):(n*i)+n:])
print(answer)
# for i in range(1, len(words)):
#     if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
#         print(i%n+1,i // n)
# else:
#     print(0, 0)