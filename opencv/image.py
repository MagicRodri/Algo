import cv2 as cv
import sys
import imutils

img = cv.imread('imgs/img.jpg',1)

if img is None:
    sys.exit('Could not read the image.')

cv.imshow('Display window',img)
k = cv.waitKey(0)

if k == ord('s'):

    #This resize the image but with distortion
    smaller=cv.resize(img,(800,800))
    cv.imwrite('imgs/resized.png',smaller)

    #To keep the aspect ratio
    ratio_smaller = imutils.resize(img,height=800)
    cv.imwrite('imgs/resized2.png',ratio_smaller)