## Python bisect 함수
bisect 는 흔히 정렬된 시퀀스를 관리하기위해 사용한다.<br>
bisec에 작동방식은 bisect.bisect(정렬된시퀀스, 추가할시퀀스)로 기존에 정렬된 시퀀스에<br>
추가할 시퀀스에 삽입할 인덱스를 반환한다.<br>
```
def grade(score, breakpoint=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoint,score)
    return grades[i]
print([grade(score) for score in [33, 99, 77, 65, 82, 92]])

> ['F', 'A', 'C', 'D', 'B', 'A']
```

bisect.insert()는 정렬된 시퀀스에 추가할 시퀀스를 추가한다.
```
import bisect
import random

SIZE = 11
random.seed(1729)
my_list =[]
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)
```