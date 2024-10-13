# -*- coding: utf-8 -*-

import numpy as np
import cv2

# cap = cv2.VideoCapture('viptrain.avi')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1)
    sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
    sobely = cv2.convertScaleAbs(sobely)
    frame = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    # frame=cv2.Canny(frame,100,200)
    cv2.imshow("frame", frame)
    c = cv2.waitKey(10)
    if c == 27:  # ESC键
        break
cap.release()
cv2.destroyAllWindows()
