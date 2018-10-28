import cv2
import numpy as np

#load image in grayscale
#1, 0 for color grayscale image respectively. by default this function read color image
img=cv2.imread('dog.jpg',1)
print(img)

#modify the image
img=img*2

#write it to file
cv2.imwrite('dogchng.jpg',img)

#display the image
cv2.imshow('imgagewindow',img) #windowname, image
cv2.waitKey(0)  
cv2.destroyAllWindows()
