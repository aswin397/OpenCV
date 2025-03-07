import cv2
img = cv2.imread('Hotel.jpg',1)
cv2.imshow('images',img)

print(img) #for pixels in terminal

cv2.waitKey(5000)  #5 seconds
cv2.destroyAllWindows()

