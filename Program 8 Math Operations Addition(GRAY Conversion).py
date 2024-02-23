import cv2 as cv
import numpy as np
import headers as hd

hd.mainhead('Colorspace Converter: RGB -> Gray')
hd.subhead('Relation Used for Conversion:')
print('\n0.299 R + 0.587 G + 0.114 B')
#Image
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 1.png"
#imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Matrix Understanding Case 1.png"
#Reading the Image
image=cv.imread(imagePath)
cv.namedWindow('Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Image',image)

hd.mainhead('Activity')
print('\n**Image Window is successfully generated**')
print('\n>>Press \'C\' key to convert colorspace of image window<<')
cv.waitKey(0)

red=image[:,:,2]
green=image[:,:,1]
blue=image[:,:,0]

#Grayscale conversion factor

red=red*0.299
green=green*0.587
blue=blue*0.114

#Gray Image Generation

Gray=np.float16(red)+np.float16(green)+np.float16(blue)
Gray=np.round(Gray,0)
Gray=np.uint8(Gray)

cv.namedWindow('Grayscale Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Grayscale Image',Gray)
print('\n**Grayscale Image Window is successfully generated**')
print('\n**Gray Image Matrix**\n')
print(Gray)
print('\n>>Press \'ESC\' key to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
hd.mainhead('Thank You!! Have a Nice Day :)')

