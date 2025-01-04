import cv2 as cv
import numpy as np
from utils import get_color_limits
from PIL import Image

yellow = [0,255,255] 

yellow_Upper, yellow_lower = get_color_limits(yellow)
black = [0,0,0]
B_upper, B_lower = get_color_limits(black)
capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    hsvframe = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsvframe,yellow_lower,yellow_Upper)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),thickness=3)
    cv.imshow("Live",frame)

    if (cv.waitKey(1) & 0xFF ==ord('q')):
        break

capture.release()
cv.destroyAllWindows()

