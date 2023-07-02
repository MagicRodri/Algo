import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Can not open camera')
    exit()
    # Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('videos/output.avi', fourcc, 24.0, (640,480))

while True:
    # Capture frame by frame
    captured,frame = cap.read()

    if not captured:
        print("Can't receive frame. Exiting...")
        break

    print(f"Frame's (width,height):({cap.get(cv.CAP_PROP_FRAME_WIDTH)},{cap.get(cv.CAP_PROP_FRAME_HEIGHT)})")

    out.write(frame)
    # Convert each captured frame to gray
    # frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame',frame)

    if cv.waitKey(1)  == ord('q'):
        break

# When everything is done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()
