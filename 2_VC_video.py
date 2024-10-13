# -*- coding: utf-8 -*-

import numpy as np
import cv2
cap = cv2.VideoCapture('video.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    # 將圖片轉為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    #cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c==27:   #ESC键
        break
cap.release()
cv2.destroyAllWindows()