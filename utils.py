import numpy as np
import cv2 as cv

def get_color_limits(color):

    c = np.uint8([[color]])

    hsvc = cv.cvtColor(c,cv.COLOR_BGR2HSV)

    lowerLimit = hsvc[0][0][0] - 10, 100, 100
    upperLimit = hsvc[0][0][0] + 10, 255,255

    lowerLimit = np.array(lowerLimit, dtype= np.uint8)
    upperLimit = np.array(upperLimit, dtype= np.uint8)

    return upperLimit,lowerLimit
