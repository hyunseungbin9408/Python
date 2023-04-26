## 지능형 리스트를 이용하여 간결하게 리스트 구성
symbols = '$#@#$'
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) < 127]
symbol_list = [symbol for symbol in symbols]

## 데카르트 곱을 지능형리스트로 구성
symbol_ascii = [(ascii, symbol) for ascii in beyond_ascii for symbol in symbols ]