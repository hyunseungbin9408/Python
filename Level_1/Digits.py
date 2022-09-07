x = 1234
j = str(x)
result = 0
for i in j:
    result += int(i)
return (if x % result == 0)