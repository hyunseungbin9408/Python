n = 5
m = 3

result = 0
if n == m or n < m:
    for i in range(n,m+1):
        result += i
else:
    for i in range(m,n+1):
        result += i
print(result)