import cv2

image_path = "qrcode_example.png"

img = cv2.imread(image_path)

detector = cv2.QRCodeDetector()

data, bbox, _ = detector.detectAndDecode(img)
print("QR  :", data)
