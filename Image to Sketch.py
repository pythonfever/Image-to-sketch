# importing library
import cv2

# image to sketch
image = cv2.imread("image.jpg")
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale = 240.0)
cv2.imwrite("sketch.png", sketch)
cv2.imshow("Image",image)

cv2.imshow("sketch", sketch)
cv2.waitKey(0) 
cv2.destroyAllWindows() 

