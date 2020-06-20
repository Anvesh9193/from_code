import cv2
import numpy as np
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img = cv2.imread("lena.jpg")
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = faceCascade.detectMultiScale(imgray,1.1,4)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
#
#
# cv2.imshow("lena",img)
# cv2.waitKey(0)


######## virtual paint
cap = cv2.VideoCapture(0)  # 0 is for single camera
cap.set(3,640)     # width
cap.set(4,480)     # Height
cap.set(10,200)    # brightness

myColors = [[5,107,0,19,255,255],                           #orange sketch pen cap   1st 3 are Hue sat and val min,last 3 are max
            [133,56,0,159,156,255],                         #Purple
            [57,76,0,100,255,255],                          #green
            [90,48,0,118,255,255]]
myColorValues = [[51,153,255],          ## BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

def findcolour(img, mycolors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array(mycolors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("image",mask)
while True:
    success, img = cap.read()   ### success is a (Boolean) variable to store
    findcolour(img,myColors)
    cv2.imshow("Video",img)
    if cv2.waitKey(5000) & 0xFF==ord('q'):
        break




   ### benjaminlechnerros@gmail.com 