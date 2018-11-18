import numpy as np
import matplotlib.pyplot as plt

import cv2

ddepth = cv2.CV_8U
kernel_size = 300
img = cv2.imread('coins_5.jpg')

#img = np.asarray(img,np.uint8)

#img = np.unicode(img)
#img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #color coreectness regarding OpenCV reversed representation of BRG instead of RGB 
#MISBEHAVING !!!!

grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow('irigion',img)

#numpy_horizontal_concat = np.concatenate((img, grayImage), axis=1)

median = cv2.medianBlur(grayImage,7) #MedianFilter to Reduce Noise DIDN"T FIND SMOOTH()
edges = cv2.Canny(median,250,280)


#Min and Max Numbers are based roughly on the Pixel size of each coin radius
Quarter = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=115)
Half_pound = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=110,maxRadius=140)

Pound = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=130,maxRadius=140)

#Change encoding to fit in circle method 


Quarter = np.uint16(np.around(Quarter))   
Half_pound = np.uint16(np.around(Half_pound))
Pound = np.uint16(np.around(Pound))

# drawing colored circle on each output points
for i in Quarter[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

for i in Half_pound[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,0,255),2)

for i in Pound[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)


img = cv2.resize(img, (880, 880))                    # Resize image
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
