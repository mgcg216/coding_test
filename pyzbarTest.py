
# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2
import numpy as np

cap = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    def lets_filter(frame, crop=False, resize=False, adaptive=False, gray=False, hist=False, bw=False, gaus3=False,
                    gaus5=False, sharp=False):
        def cropper(scale_percent, image):
            scale = scale_percent / 100
            ow = int(image.shape[1])
            oh = int(image.shape[0])

            w = int(ow * scale)
            h = int(oh * scale)

            y = int(oh / 2 - h / 2)
            x = int(ow / 2 - w / 2)
            coorArr = [x, y, x + w, y + h]
            crop_image = image[y:y + h, x:x + w]
            return crop_image, coorArr
        if crop is True:
            frame, cropArr = cropper(50, frame)
        elif crop is False:
            cropArr = 0
        if resize is True:
            scale_percent = 30
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
            frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        if gray is True or bw is True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if gray is True and hist is True:
            frame = cv2.equalizeHist(frame)
        if adaptive is True:
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            frame = cv2.fastNlMeansDenoising(frame, None, 12, 12, 7)
            frame = cv2.bilateralFilter(frame, 9, 75, 75)

            # frame = cv2.medianBlur(frame, 5)
            frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            #                            cv2.THRESH_BINARY, 11, 2)
            # (thresh, frame) = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        if bw is True:
            (thresh, frame) = cv2.threshold(frame, 175, 255, cv2.THRESH_BINARY)
        if gaus3 is True:
            frame = cv2.GaussianBlur(frame, (3, 3), 0)
        if gaus5 is True:
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
        if sharp is True:
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
            frame = cv2.filter2D(frame, -1, kernel)
        return frame, cropArr

    filteredFrame, cropArr = \
        lets_filter(frame, crop=False, resize=True, adaptive=False, bw=True, gaus3=False, sharp=False)

    # for i in range(3):
    #     frame[cropArr[1]:cropArr[3], cropArr[0]:cropArr[2], i] = filteredFrame

    image = filteredFrame
    barcodes = pyzbar.decode(image)


    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    # Display the resulting frame
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

