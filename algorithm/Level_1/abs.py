absolutes = [4,7,12]
signs = ['true','false','true']
result = 0

for i in range(len(absolutes)):
    if signs[i] == "true":
        result += absolutes[i]
    else:
        result -= absolutes[i]
print(result)