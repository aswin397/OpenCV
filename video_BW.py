import cv2
capture = cv2.VideoCapture(0)  # 0 only for 1 camera
while True:
    ret, frame = capture.read(0)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

capture.release()
cv2.destroyAllWindows()