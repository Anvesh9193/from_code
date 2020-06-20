#read and write a image
import cv2
import numpy as np
from stackImages import *

# img = cv2.imread("lena.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(4000)
###### webcam access/ reading through a web cam
""" cap = cv2.VideoCapture(0)  # 0 is for single camera
cap.set(3,640)     # width
cap.set(4,480)     # Height
cap.set(10,100)    # brightness
while True:
    success, img = cap.read()   ### success is a (Boolean) variable to store
    cv2.imshow("Video",img)
    if cv2.waitKey(5000) & 0xFF==ord('q'):
        break """

# img = cv2.imread("lena.jpg")
# kernel = np.ones((5,5),np.uint8)         # defining matrix 5*5 and type integer of size 8 bits i.e 255 pixels
#
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# imgcanny = cv2.Canny(img, 100,100)
# imgcanny2 = cv2.Canny(img,100,150)
# imgdilation = cv2.dilate(imgcanny, kernel, iterations=1)  #iterations is thickness
# imgeroded = cv2.erode(imgdilation, kernel,iterations=1)   # reduce the thickness


# cv2.imshow("Blur img", imgBlur)
# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Canny", imgcanny)
# cv2.imshow("can",imgcanny2)
# cv2.imshow("image", img)
# cv2.imshow("Dilated", imgdilation)
# cv2.imshow("eroded", imgeroded)
# cv2.waitKey(0)


# newimg = cv2.imread("thumb.jpg")
# print(newimg.shape)                ## output is (1333, 827, 3) where height , width, channels i.e bgr
# newimgr = cv2.resize(newimg,(300,200))
# imgcrop = newimg[0:200,200:500]  # height 1st
# cv2.imshow("thumb",newimg)
# cv2.imshow("resized",newimgr)
# cv2.imshow("cropped",imgcrop)
# cv2.waitKey(0)

### draw shapes and write texts on image
## we use numpy


""" img = np.zeros((512,512,3),np.uint8)    # black image with size 512,512 and colour function 3
img[:] = 255,0,0                       # croping function for blue colour(colouring whole)
img[200:300, 100:300] = 255,0,0         # cropping blue to limited range

cv2.line(img,(0,0),(300,300),(0,255,0),3)   # 3 is the thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  # line for full image
cv2.rectangle(img,(0,0),(250,350),(0,0,255))
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)  # to fill the rectangle
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)  # 0.5 is thickness
cv2.imshow("new",img)
cv2.waitKey(0) """


### joining images
# def getcontours(img):
#     contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)               ###RETR_EXTERNAl will retriveall outer contours
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area) 
#         if area > 500:
#             cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt, True)
#             print(peri)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)                   #approx will give the points of the corners of each shape
#             print(len(approx))
#             objcorners = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)                   #gives the values for each of shape
#
#             if objcorners ==3: objectType = "Triangle"
#             elif objcorners == 4:
#                     if w/float(h)==1: objectType = "Square"
#                     else: objectType = "Rectangle"
#
#             else: objectType="circle"
#             cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
#             cv2.putText(imgcontour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)

#
# img = cv2.imread('shapes.png')
# imgcontour = img.copy()
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
# imgcanny = cv2.Canny(imgBlur,50,50)
#
# getcontours(imgcanny)
#
# imgblank = np.zeros_like(img)
# imgstack = stackImages(0.6,([img,imgGray,imgBlur],[imgcanny,imgcontour,imgblank]))
# cv2.imshow("stack",imgstack)
# cv2.waitKey(0)
# imghor = np.hstack((img,img))
# imver= np.hstack((img,img))
# cv2.imshow('new',imver)
# cv2.waitKey(0)

## detection of colour

def empty(a):
     pass


img = cv2.imread('lena.jpg')
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",0,179,empty)
cv2.createTrackbar("sat Min","TrackBars",0,179,empty)
cv2.createTrackbar("sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("val Min","TrackBars",0,179,empty)
cv2.createTrackbar("val Max","TrackBars",255,255,empty)


while True:
     img = cv2.imread('lena.jpg')
     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
     h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
     h_max = cv2.getTrackbarPos("Hue Min", "TrackBars")
     s_min = cv2.getTrackbarPos("sat Min", "TrackBars")
     s_max = cv2.getTrackbarPos("sat Max", "TrackBars")
     v_min = cv2.getTrackbarPos("val Min", "TrackBars")
     v_max = cv2.getTrackbarPos("val Max", "TrackBars")
     lower = np.array([h_min,s_min,v_min])
     upper = np.array([h_max,s_max,v_max])
     mask = cv2.inRange(imgHSV,lower,upper)

     cv2.imshow("original",img)
     cv2.imshow('new',imgHSV)
     cv2.imshow("mask",mask)
     cv2.waitKey()
















