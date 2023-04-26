

participant = ["mislav", "stanko", "mislav", "ana"]
completion= ["stanko", "ana", "mislav"]

count = 0



import collections
name = collections.Counter(participant) - collections.Counter(completion)
print(list(name.keys())[0])