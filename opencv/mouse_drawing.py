import numpy as np
import cv2 as cv
import math
drawing = False # true if mouse is pressed
drawRectangle = True # if True, draw rectangle. Press 'm' to toggle to curve
drawCircle = True # if True, draw circle
ix,iy = -1,-1

img = np.zeros((512,512,3), np.uint8)
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,drawRectangle,drawCircle

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            # Show the drawing process while mouse pressed and moving
            if drawRectangle:
                # cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                cv.line(img,(ix,iy),(ix,y),(0,255,0),1)
                cv.line(img,(ix,iy),(x,iy),(0,255,0),1)
                
            elif drawCircle:
                r = math.sqrt(pow(x-ix,2)+pow(y-iy,2))
                cv.circle(img,(ix,iy),int(r),(255,0,0),-1)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        # Final drawing when mouse released
        if drawRectangle:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        elif drawCircle:
            r = math.sqrt(pow(x-ix,2)+pow(y-iy,2))
            cv.circle(img,(ix,iy),int(r),(255,0,0),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1)
    if k == ord('m'):
        drawRectangle = not drawRectangle
    elif k == ord('c'):
        drawCircle = not drawCircle
    elif k == ord('q'):
        break
cv.destroyAllWindows()