#Color Splasher using Trackbar: RGB Colorspace

import numpy as np
import cv2 as cv
import headers as hd

#necessary function argument to pass in trackbar()
def necessaryArg(x):
    pass

hd.mainhead('Color Splasher using Trackbar')
hd.subhead('User Input Required:')
print('\nNote:For better results and visualization choose H=256 and W=256\n')

#Input the Resolution
rows=int(input('Enter the Height of the Viewer Window: '))
cols=int(input('\nEnter the Width of the Viewer Window: '))
hd.mainhead('Activity')
print('\n**Color splasher with trackbars successfully generated**')
print('\n**Please "ON" the first trackbar to see effects on splasher**')
print('\n**Now move the slider of red trackbar to get new splash**')
print('\n>>Press \'ESC\' key to close Color Splasher Window<<')

#Matrix Generation for Blue, Green and Red Channel
#Blue
blue=np.matrix(np.ones([rows,cols]))
multiplierBlue=np.uint8(np.matrix(np.arange(0,cols,1)))
blueMatrix=np.multiply(blue,multiplierBlue)
blueChannel = np.uint8(blueMatrix)
#Green
green=np.matrix(np.ones([rows,cols]))
multiplierGreen=np.uint8(np.matrix(np.arange(0,rows,1)))
multiplierGreenT=multiplierGreen.transpose()
greenMatrix=np.multiply(green,multiplierGreenT)
greenChannel = np.uint8(greenMatrix)
#Red
redBrightValue=0          #Initialized Value
redChannel = np.uint8(np.ones([rows,cols])*redBrightValue)    

#Splash Maker(Initialized View when brightness value of red is 0)
colorSplash = cv.merge([blueChannel,greenChannel,redChannel])

#Window Intialization
cv.namedWindow('Color Splasher',cv.WINDOW_FREERATIO)

#Switch for ON/OFF functionality of trackbar
switchMode='0:OFF\n1:ON'
cv.createTrackbar(switchMode,'Color Splasher',0,1,necessaryArg)

#Create trackbar for changing red brightness value
cv.createTrackbar('Red','Color Splasher',0,255,necessaryArg)

previousBrightnessVal=0
while True:
    cv.imshow('Color Splasher',colorSplash)
    key=cv.waitKey(5)
    if key==27:
        break

    #get current positions of both trackbars
    redBrightValue=cv.getTrackbarPos('Red','Color Splasher')
    switch=cv.getTrackbarPos(switchMode,'Color Splasher')
    
    if switch==0:
        redBrightValue=previousBrightnessVal
        redChannel = np.uint8(np.ones([rows,cols])*redBrightValue) 
        colorSplash = cv.merge([blueChannel,greenChannel,redChannel])
    else:
        redChannel = np.uint8(np.ones([rows,cols])*redBrightValue) 
        colorSplash = cv.merge([blueChannel,greenChannel,redChannel])
        previousBrightnessVal=redBrightValue

cv.destroyWindow('Color Splasher')
print('\n**Color splasher results successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day :)')

