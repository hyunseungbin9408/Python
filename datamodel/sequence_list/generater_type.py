import array
## 제너레이터 표현식를 이용하여 간결하게 리스트 구성
symbols = '$#@*&'
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) < 127]
tuple(ord(symbol) for symbol in symbols)

array.array('i',(ord(symbol) for symbol in symbols)) ## array('i', [36, 35, 64, 42, 38])
for cola in ('%s %s' % (ascii, symbol) for ascii in beyond_ascii for symbol in symbols):
    print(cola)

