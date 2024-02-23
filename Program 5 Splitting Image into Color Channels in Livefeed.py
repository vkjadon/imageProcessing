import numpy as np
import cv2 as cv
import headers as hd

#Variable for vision source feed
visionSource=cv.VideoCapture(0)

#Heading
hd.mainhead('Live Feed: Splitted Image Channels')
print('\nAction Required is represented by: >>')

#Checking for whether the vision source selected is present or not.
if visionSource.isOpened():
    returnFromReadFun,frame=visionSource.read()
    hd.mainhead('Activities')
else:
    returnFromReadFun=False
    hd.mainhead('!!ALERT!!')
    print('**Required Action**\n\nPlease Select the valid Vision Source')
    #cv.waitKey(10)
    exit()

print('\n**Live Feed Windows are successfully generated**')
print('\n>>Press "Esc" on any Live Feed Window to Close')

while returnFromReadFun:

    returnFromReadFun,frame=visionSource.read()

    blueChannel=frame[:,:,0]
    greenChannel=frame[:,:,1]
    redChannel=frame[:,:,2]

    cv.imshow('Live Feed: RGB Colorspace',frame)
    cv.imshow("Live Feed: Blue Channel",blueChannel)
    cv.imshow("Live Feed: Green Channel",greenChannel)
    cv.imshow("Live Feed: Red Channel",redChannel)

    #if we want to exit out from the live feed
    k=cv.waitKey(1)
    if k==27:
        break

cv.destroyAllWindows()
print('\n**Live Feed Windows are successfully closed**')

hd.mainhead('Thank You!! Have a Nice Day :)')
#Release the Vision Source
visionSource.release()

