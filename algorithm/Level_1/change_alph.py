
s = "one4seveneight"
number = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight','9':'nine'}

result = ""
for i,j in enumerate(number.values()):
    if s.find(j) != -1:
        s = s.replace(j,str(i))
print(s)