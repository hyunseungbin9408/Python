from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
seoul = City('Seoul','KR', 36.933, (35.689722, 139.691667))
tokyo = City('tokyu','JP', 36.933, (35.689722, 139.691667))
make_city = City._make(tokyo)
print(make_city.__add__(City._make(seoul)))

