import cv2
import numpy as np

path = "/Users/ruppikha/PycharmProjects/OpenCV-Project/Resources/both.jpeg"

def team(n):
    if n == 0:
        name = "Portugal"
        lower = (0, 90, 70)
        upper = (10, 255, 255)
        return (name, lower, upper)
    if n == 1:
        name = "Brazil"
        lower = (20, 100, 100)
        upper = (30, 255, 255)
        return (name, lower, upper)

img=cv2.imread(path)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

for i in range(2):
    name,lower,upper=team(i)
    mask=cv2.inRange(hsv, lower, upper)
    contour,her=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    big=sorted(contour,key=cv2.contourArea,reverse=True)[0]
    rect=cv2.boundingRect(big)
    x,y,w,h=rect
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,23,0),2)
    cv2.putText(img,name, (x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,23,0))


cv2.imshow("Image",img)
#cv2.imshow("Mask",mask)
cv2.waitKey(0)
