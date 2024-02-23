#Module Import
import cv2 as cv
import numpy as np
import headers as hd

#Variable for vision source feed
visionSource=cv.VideoCapture(2)

#Heading
hd.mainhead('Program: Live Feed From Camera')
print('\nAction Required is represented by: >>')

#Version Check
hd.mainhead('Version of Modules')
print('\nThe version of imported OpenCV\'s module:',cv.__version__)
print('\nThe version of imported Numpy\'s module:',np.__version__)

#Checking for whether the vision source selected is present or not.
#print(visionSource.isOpened())

if visionSource.isOpened():
    returnFromReadFun,frame=visionSource.read()
    hd.mainhead('Activities')
else:
    returnFromReadFun=False
    hd.mainhead('!!ALERT!!')
    print('**Required Action**\n\nPlease Select the valid Vision Source')
    #cv.waitKey(10)
    exit()

#>>Till here you can also check that you got a single frame(image)<<
#Video is defined as a series of single frames(images)
print('\n**Live Feed Window is successfully generated**')
print('\n>>Press "Esc" on Live Feed Window to Close')

#How to show the live feed(Continual frame showing)
while returnFromReadFun:

    returnFromReadFun,frame=visionSource.read()

    cv.imshow('Live Feed',frame)

    #if we want to exit out from the live feed
    k=cv.waitKey(1)
    if k==27:
        break

cv.destroyWindow('Live Feed')
print('\n**Live Feed Window is successfully closed**')

hd.mainhead('Thank You!! Have a Nice Day :)')

#Release the Vision Source
visionSource.release()
