#Color Palette: RGB Colorspace

import numpy as np
import cv2 as cv
import headers as hd

hd.mainhead('Color Palette: RGB Colorspace')
hd.subhead('User Input Required:')

#Input the Resolution
rows=int(input('Enter the Height(Rows) of the Palette Window: '))
cols=int(input('\nEnter the Width(Columns) of the Palette Window: '))

#Matrix Generation of B-G-R
blueChannel = np.uint8(np.random.randint(255,size=(rows,cols)))
greenChannel = np.uint8(np.random.randint(255,size=(rows,cols)))     
redChannel = np.uint8(np.random.randint(255,size=(rows,cols)))   

hd.mainhead('Activity')
#Color Maker
color = cv.merge([blueChannel,greenChannel,redChannel])
cv.namedWindow('Color Palette',cv.WINDOW_KEEPRATIO)
cv.imshow('Color Palette',color)

print('\n**Color palette results successfully generated**')
print('\n**Color Palette Matrix**\n')
print(color)
print('\n>>Press \'ESC\' key to close Color Palette Window<<')
cv.waitKey(0)
cv.destroyWindow('Color Palette')
print('\n**Color palette results successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day :)')

