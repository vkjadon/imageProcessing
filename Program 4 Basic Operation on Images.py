import cv2 as cv
import numpy as np
import headers as hd

#Heading
hd.mainhead('Program: Splitting of Image Channels')
print('\nAction Required is represented by: >>')

#Version Checking
hd.mainhead('Version of Modules')
print('\nThe version of imported OpenCV\'s module:',cv.__version__)
print('\nThe version of imported Numpy\'s module:',np.__version__)
hd.mainhead('Activities')

#Specifying Image Path
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Matrix Understanding Case 2.png"

#Reading the Image
image=cv.imread(imagePath)

#Window Creation for displaying with different view options
cv.namedWindow('Read Image',cv.WINDOW_KEEPRATIO)
#Showing the Image
cv.imshow('Read Image',image)
print('\n**Image Window is successfully generated**')
print('\n>>Press \'P\' key on Image Window and have a look on Image Properties<<')

#Waiting for key press
cv.waitKey(0)       

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
print('\nThe Image Matrix or Array(in BGR):\n',image)

hd.mainhead('Activities')
print('\n**Image Properties is successfully generated**')
print('\n>>Press \'S\' key on Image Window to split and view splitted channels of Image')
cv.waitKey(0)

#Splitting Channels
hd.mainhead('Splitted Image Matrices')
print('\n**Red Channel Matrix**')
red=image[:,:,2]
print(red)
cv.namedWindow('Red Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Red Channel Matrix',red)
print('\n**Green Channel Matrix**')
green=image[:,:,1]
print(green)
cv.namedWindow('Green Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Green Channel Matrix',green)
print('\n**Blue Only Matrix**')
blue=image[:,:,0]
print(blue)
cv.namedWindow('Blue Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Blue Channel Matrix',blue)
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfullly closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')

