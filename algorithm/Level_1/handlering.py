strings = ["abce", "abcd", "cdx"]
n = 2
strings.sort()
print(sorted(strings,key=lambda x : x[n]))