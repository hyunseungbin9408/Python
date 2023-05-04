import bisect
import sys

def grade(score, breakpoint=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoint,score)
    return grades[i]
print([grade(score) for score in [33, 99, 77, 65, 82, 92]])

import bisect
import random

SIZE = 11
random.seed(1729)
my_list =[]
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)
