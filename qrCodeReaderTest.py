import cv2
droidcam = "http://100.81.42.151:4747"
def video_reader():
    cam = cv2.VideoCapture(2)
    detector = cv2.QRCodeDetector()  #QRCode detector
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code detected-->", data)
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("Q"):
            break
    cam.release()
    cv2.destroyAllWindows()


video_reader()