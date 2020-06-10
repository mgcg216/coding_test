import numpy as np
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\michael.guerrero\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Display the resulting frame
    cv2.imshow('frame', frame)
    text = tess.image_to_string(frame)
    print(text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everythin is done, release teh capture
cap.release()
cv2.destroyAllWindows()
