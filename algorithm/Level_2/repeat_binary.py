s = "110010101001"
result_repeat = 0
result_remove_zero = 0
string = ""
while len(s) > 1:
    for i in s:
        if i == '0':
            result_remove_zero += 1
        else:
            string += '1'
    s = bin(len(string))[2:]
    string = ''
    result_repeat += 1
print(result_repeat,result_remove_zero)
