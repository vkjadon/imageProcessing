#Introduction to OpenCV
import cv2 as cv
import numpy as np
import headers as hd

#Program Head
hd.mainhead('Program: Getting Started with Images')

#Version Checking
hd.mainhead('Version of Modules')
print('\nThe version of imported OpenCV\'s module:',cv.__version__)
print('\nThe version of imported Numpy\'s module:',np.__version__)

hd.mainhead('Activities')

#Specifying Image Path
imagePath="D:\\edu\\Masters\\Robotics and Humanoids\\Vision\\Python Programs\\testImage.jpg"
#imagePath1="testImage.jpg"

#Reading the Image
image=cv.imread(imagePath)

#Window Creation for displaying with different view options
#cv.namedWindow('Read Image',cv.WINDOW_KEEPRATIO)
#cv.namedWindow('Read Image')
#Showing the Image
cv.imshow('Read Image',image)

print('\n**Image Window is successfully generated**')
print('\n>>Press any key to close Image Window and have a look on Image Properties<<')

#Closing of Image Window with key press
cv.waitKey(0)       #0 is special case in which the statement wait forever. In general the arguement within parenthesis is delay time in ms.
cv.destroyWindow('Read Image')

print('\n**Image Window is successfully closed**')

#Image Properties
hd.mainhead('Image Properties')
    #Data Type
print('\nThe Data Type of Image:',image.dtype)
    #Shape of Image
print('\nThe Shape of Image:',image.shape)
    #Dimension of Image
print('\nThe Dimension of Image:',image.ndim)
    #Size of Image
print('\nThe Size of Image(in bytes):',image.size)
    #Type of Image Matrix
print('\nThe type of Image Variable:',type(image))
    #Image Matrix
print('\nThe Image Matrix or Array:\n',image)
