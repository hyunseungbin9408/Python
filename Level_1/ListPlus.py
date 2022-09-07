
arr1 = [[1,4],[2,7]] # arr2 = [[5,6],[3,1]]
arr2 = [[5,6],[3,1]]

result_return = []
for i in range(len(arr1)):
    result = []
    for j in range(len(arr1[0])):
        result.append(arr1[i][j] + arr2[i][j])
    result_return.append(result)
print(result_return)