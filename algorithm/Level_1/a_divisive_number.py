arr = [5, 9, 7, 10]
n = 5
result_arr = []

for i in arr:
    if i % n == 0:
        result_arr.append(i)
print(len(result_arr))