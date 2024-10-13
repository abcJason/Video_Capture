import numpy as np
import cv2

cap = cv2.VideoCapture("video.avi")
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("output1.mp4", fourcc, 20, (width, height))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
