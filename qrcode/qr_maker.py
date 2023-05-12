import pyqrcode
# url = pyqrcode.create('http://uca.edu')
# url.svg('uca-url.svg', scale=8)
# url.eps('uca-url.eps', scale=2)
# print(url.terminal(quiet_zone=2))

#data = "WIFI:S:SK_WiFiGIGA1E1F;T:WPA;P:2006003493"
data = "BEGIN:VCARD\n"
data += "VERSION:3.0\n"
data += "FN:현승빈\n"
data += "TEL;TYPE=WORK;CELL:010 7393 3333\n"
data += "EMAIL;TYPE=WORK:abce@naver.com\n"
data += "URL;TYPE=WORK:https://www.naver.com\n"
data += "END:VCARD\n"

qrcode = pyqrcode.create(data, error="L", version=7, mode="binary", encoding='utf-8')
qrcode.png("qr_cloocus.png", scale=10, module_color=(0,0,0,255), background=[255,255,255,255])
qrcode.show()

