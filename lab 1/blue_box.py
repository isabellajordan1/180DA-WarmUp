
# used the following links to start code
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
# I combined the two to use the mask from the first and the ability to get a box from the latter

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    rect = frame
    contours,hierarchy = cv.findContours(mask, 1, 2)
    if (contours):
        max_contour = max(contours, key = cv.contourArea)
        x,y,w,h = cv.boundingRect(max_contour)
        rect = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
