#Color Viewer: RGB Colorspace

import numpy as np
import cv2 as cv
import headers as hd

hd.mainhead('Color Splasher: RGB Colorspace')
hd.subhead('User Input Required:')

#Input the Resolution
rows=int(input('Enter the Height of the Viewer Window: '))
cols=int(input('\nEnter the Width of the Viewer Window: '))
#Matrix Generator
blue=np.matrix(np.ones([rows,cols]))
multiplierBlue=np.uint8(np.matrix(np.arange(0,cols,1)))
green=np.matrix(np.ones([rows,cols]))
multiplierGreen=np.uint8(np.matrix(np.arange(0,rows,1)))
multiplierGreenT=multiplierGreen.transpose()
blueMatrix=np.multiply(blue,multiplierBlue)
greenMatrix=np.multiply(green,multiplierGreenT)
#print(blueMatrix)
#print(greenMatrix)
#Matrix Generation of B-G-R
redBrightValue=180
blueChannel = np.uint8(blueMatrix)
greenChannel = np.uint8(greenMatrix)
redChannel = np.uint8(np.ones([rows,cols])*redBrightValue) 
#redChannel = np.uint8(np.random.randint(255,size=(rows,cols)))   

hd.mainhead('Activity')
#Color Maker
color = cv.merge([blueChannel,greenChannel,redChannel])
#color = cv.merge([redChannel,blueChannel,greenChannel])
#color = cv.merge([greenChannel,redChannel,blueChannel])
cv.namedWindow('Color Splasher',cv.WINDOW_KEEPRATIO)
cv.imshow('Color Splasher',color)

print('\n**Color splasher results successfully generated**')
print('\n>>Press \'ESC\' key to close Color Viewer Window<<')
cv.waitKey(0)
cv.destroyWindow('Color Splasher')
print('\n**Color splasher results successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day :)')

