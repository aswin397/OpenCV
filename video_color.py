import cv2
capture = cv2.VideoCapture(0)  # 0 only for 1 camera
while True:
    ret, frame = capture.read(0)
    cv2.imshow('image',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()