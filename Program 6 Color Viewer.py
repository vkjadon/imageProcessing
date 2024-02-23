#Color Viewer: RGB Colorspace

import numpy as np
import cv2 as cv
import headers as hd

hd.mainhead('Color Viewer: RGB Colorspace')
hd.subhead('User Input Required:')

#Input the Resolution
rows=int(input('Enter the Height of the Viewer Window: '))
cols=int(input('\nEnter the Width of the Viewer Window: '))

#Input the R-G-B
print('\n**Note: Please enter the brightness values between(0-255)**')
blueBrightValue=int(input('\nEnter the Brightness Value of Blue Channel: '))
greenBrightValue=int(input('\nEnter the Brightness Value of Green Channel: '))
redBrightValue=int(input('\nEnter the Brightness Value of Red Channel: '))

#Matrix Generation of B-G-R
blueChannel = np.uint8(np.ones([rows,cols])*blueBrightValue)
greenChannel = np.uint8(np.ones([rows,cols])*greenBrightValue)     
redChannel = np.uint8(np.ones([rows,cols])*redBrightValue)    

hd.mainhead('Activity')
#Color Maker
color = cv.merge([blueChannel,greenChannel,redChannel])
#cv.namedWindow('Color Viewer',cv.WINDOW_KEEPRATIO)
cv.imshow('Color Viewer',color)

print('\n**Color viewer results successfully generated**')
print('\n>>Press \'ESC\' key to close Color Viewer Window<<')
cv.waitKey(0)
cv.destroyWindow('Color Viewer')
print('\n**Color viewer results successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day :)')

