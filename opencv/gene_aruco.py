import cv2 as cv
import numpy as np

# Load the predefined dictionary
dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Generate the marker
markerImage = np.zeros((200,200),dtype=np.uint8)
markerImage = cv.aruco.drawMarker(dictionary,33,200,markerImage,5)

# Detector parameters using default values
parameters = cv.aruco.DetectorParameters_create()

# Detection
corners, ids, rejected = cv.aruco.detectMarkers(markerImage,dictionary,parameters=parameters)
print(corners,ids,rejected)
cv.imshow('',markerImage)
cv.imwrite('marker33.png',markerImage)