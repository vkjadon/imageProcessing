#Introduction to OpenCV

import cv2 as cv
import numpy as np
import headers as hd

hd.mainhead('Program: Image Subtraction')
print('\nAction Required is represented by: >>')
hd.mainhead('Activities')
#Specifying Image Path
#imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Matrix Understanding Case 2.png"
#imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 1.png"
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 3.png"
#imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 3.png"
#imagePath1="testImage.jpg"

#Reading the Image
image=cv.imread(imagePath)

#Window Creation for displaying with different view options
cv.namedWindow('Read Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Read Image',image)

print('\n**Image Window is successfully generated**')
print('\n>>Press \'P\' key on Image Window and have a look on Image Matrix<<')
cv.waitKey(0)      

#Image Properties
hd.mainhead('Image Matrix')
    #Shape of Image
print('\nThe Shape of Image:',image.shape)
    #Image Matrix
print('\nThe Image Matrix or Array(in BGR):\n',image)

hd.mainhead('Activities')
print('\n**Image Matrix is successfully generated**')
print('\n>>Press \'S\' key on Image Window to split and view splitted channels of Image')
cv.waitKey(0)
#Splitting Channels
hd.mainhead('Splitted Image Matrices')
print('\n**Red Channel Matrix**')
red=np.matrix(image[:,:,2])
print(red)
cv.namedWindow('Red Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Red Channel Matrix',red)
print('\n**Green Channel Matrix**')
green=np.matrix(image[:,:,1])
print(green)
cv.namedWindow('Green Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Green Channel Matrix',green)
print('\n**Blue Only Matrix**')
blue=np.matrix(image[:,:,0])
print(blue)
cv.namedWindow('Blue Channel Matrix',cv.WINDOW_KEEPRATIO)
cv.imshow('Blue Channel Matrix',blue)
hd.mainhead('Object Isolation')
print('\n>>Press \'R\' key to isolate the object with higher Red color content')
print('\nor')
print('\n>>Press \'G\' key to isolate the object with higher Green color content')
print('\nor')
print('\n>>Press \'B\' key to isolate the object with higher Blue color content')
hd.mainhead('Isolated Object Matrix')
key=cv.waitKey(0)
if(key==82 or key==114):
    red_only=np.int16(red)-np.int16(green)-np.int16(blue)
    red_only[red_only<0]=0
    red_only[red_only>255]=255
    red_only=np.uint8(red_only)
    red_only=np.uint8(red_only)
    cv.namedWindow('Higher Red Content Object',cv.WINDOW_KEEPRATIO)
    cv.imshow('Higher Red Content Object',red_only)
    hd.subhead('Object with Higher Red Content')
    print('The Isolated Object Matrix\n',red_only)
elif(key==71 or key==103):
    #green_only=np.int16(green)-np.int16(red)-np.int16(blue)
    green_only=np.int16(blue)-np.int16(red)
    green_only[green_only<0]=0
    green_only[green_only>255]=255
    green_only=np.uint8(green_only)
    cv.namedWindow('Higher Green Content Object',cv.WINDOW_KEEPRATIO)
    cv.imshow('Higher Green Content Object',green_only)
    hd.subhead('Object with Higher Green Content')
    print('The Isolated Object Matrix\n',green_only)
elif(key==66 or key==98):
    #blue_only=np.int16(blue)-np.int16(green)-np.int16(red)
    blue_only=np.int16(red)-np.int16(green)
    blue_only[blue_only<0]=0
    blue_only[blue_only>255]=255
    blue_only=np.uint8(blue_only)
    cv.namedWindow('Higher Blue Content Object',cv.WINDOW_KEEPRATIO)
    cv.imshow('Higher Blue Content Object',blue_only)
    hd.subhead('Object with Higher Blue Content')
    print('The Isolated Object Matrix\n',blue_only)
else:
    print('\nInvalid Choice')
    cv.destroyAllWindows()
    exit()
hd.mainhead('Activities')
print('\n**Isolated Image Window is successfully generated**')
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')

