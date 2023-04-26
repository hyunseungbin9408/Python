n = 10
arr = []
for i in range(1,n):
    if n % i == 1:
        arr.append(i)
print(min(arr))