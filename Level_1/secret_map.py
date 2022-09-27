arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5

bin_arr_1 = []
bin_arr_2 = []
result = []
for i in range(len(arr1)):
    bin_arr_1.append(format(bin(arr1[i])[2:]).zfill(n))
    bin_arr_2.append(format(bin(arr2[i])[2:]).zfill(n))
print(bin_arr_1,bin_arr_2)
for i in range(len(bin_arr_1)):
    result_value = ''
    for j in range(len(bin_arr_2)):
        if bin_arr_1[i][j] == '1' or bin_arr_2[i][j] == '1':
            result_value += "#"
        else:
            result_value += " "
    result.append(result_value)
print(result)
