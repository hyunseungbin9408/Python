## 튜플
lax_coorinates = (33.9435, -118.408056)
city, year, pop, chg, area = ('Seoul', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567')]

for passport in sorted(traveler_ids):
    print(passport)

## for에서 _ 더미 변수를 이용하여 국가 코드만 나오게 함
for country, _ in sorted(traveler_ids):
    print(country) ## BRA, USA

## 튜플 언패킹
latitude, longitude = lax_coorinates ## (33.9435, -118.408056)
print(latitude) ## 33.9435
print(longitude) ## -118.408056

## 튜플 언패킹으로 병렬 할당하기
t = (20, 8)
divmod(*t)

quotient, remainder = divmod(*t) ## (2,4), (2,4)
