arr = [1,2,3,4,6,7,8,0]
arr2 = [5,8,4,0,6,7,9]

result = 0
for i in range(0,10):
    if i in arr2:
        pass
    else:
        result += i
print(result)