arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
bin(11)
bin_arr_1 = []
bin_arr_2 = []

for i in range(0, len(arr1)):
    if arr1[i] < 16:
        if arr1[i] == 1:
            bin_arr_1.append('0000' + bin(arr1[i])[2:])
        else:
            bin_arr_1.append('0' + bin(arr1[i])[2:])
    if arr2[i] < 16:
        if arr2[i] == 1:
            bin_arr_2.append('0000' + bin(arr2[i])[2:])
        else:
            bin_arr_2.append('0' + bin(arr2[i])[2:])
    if arr1[i] > 16:
        bin_arr_1.append(bin(arr1[i])[2:])
    if arr2[i] > 16:
        bin_arr_2.append(bin(arr2[i])[2:])
for j in bin_arr_1:

    print(j.replace('1','#'))
#for i in bin_arr_1: