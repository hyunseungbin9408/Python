import cv2
import pyzbar.pyzbar as pyzbar

def read_qrcode_cv2(opencv_image):
    detecter = cv2.QRCodeDetector()
    data, bbox, _ = detecter.detectAndDecode(opencv_image)
    if data:
        print(f"QRCODE 데이터: {data}")
        print(f"QRCODE 위치: {bbox}")
        top_value = (int(bbox[0][0][0]), int(bbox[0][0][1]))
        bottom_value = (int(bbox[0][2][0]), int(bbox[0][2][1]))
        letftop = top_value
        rightbottom = bottom_value
        
        cv2.rectangle(opencv_image, letftop, rightbottom, (0,0,255), 5)
        cv2.imshow("tttt", opencv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def read_qrcode_zbar(opencv_image):
    gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    for d in decoded:
        x, y, w, h = d.rect
        qrcode_data = d.data.decode("utf-8")
        qrcode_type = d.type
        cv2.rectangle(opencv_image, (x,y), (x + w, y + h), (0, 0, 255), 3)
        text = f"{qrcode_data} {qrcode_type}"
        cv2.putText(opencv_image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow("tttt", opencv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
filepath_1 = ".\Python\qrcode\qr_cloocus.png"
filepath_2 = ".\Python\qrcode\qrcode_2.jpg"
cv_image_1 = cv2.imread(filepath_1)
cv_image_2 = cv2.imread(filepath_2)

# read_qrcode_cv2(cv_image_1)
# read_qrcode_cv2(cv_image_2)
# read_qrcode_zbar(cv_image_1)
# read_qrcode_zbar(cv_image_2)

def read_qrcode_webcam():
    cap = cv2.VideoCapture(1)
    i = 0
    while(cap.isOpened()):
        ret, img = cap.read()
        if not ret:
            print("ERROR")
            continue
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
        for d in decoded:
            x, y, w, h = d.rect
            qrcode_data = d.data.decode("utf-8")
            qrcode_type = d.type
            cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 3)
            text = f"{qrcode_data} {qrcode_type}"
            cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow("IMG", img)
        key = cv2.waitKey(1)
        
        if key == ord("q"):
            break
        elif key == ord("s"):
            cv2.imwrite(f"c_{i}.jpg", img)
            i += 1
    cap.release()
    cv2.destroyAllWindows()
    
read_qrcode_webcam()