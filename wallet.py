sizes =[[60, 50], [30, 70], [60, 30], [80, 40]]
result = [max(min(x) for x in sizes) * max(max(x) for x in sizes)]
print(result)
