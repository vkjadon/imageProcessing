##Live Feed From Camera and Capture the Image and Then save that image.

#Module Import
import cv2 as cv
import numpy as np
import headers as hd

#Variable for vision source feed
visionSource=cv.VideoCapture(0)

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
print('\n>>Press \'C\' on Live Feed Window to Capture the Image')

#How to show the live feed(Continual frame showing)
while returnFromReadFun:

    returnFromReadFun,frame=visionSource.read()

    cv.imshow('Live Feed',frame)

    #if we want to exit out the live feed or capture the certain frame from feed
    k=cv.waitKey(1)
    if (k==67 or k==99):
        break

print('\n**Image is successfully captured**')
cv.destroyWindow('Live Feed')
print('\n**Live Feed Window is successfully closed**')
#Showing Captured Image
cv.imshow('Captured Image',frame)
cv.waitKey(5)
print('\n**Name the Captured Image**')
imageName=input('\n>>Enter the name of Image Output(with extension):')
#Writing of Image on Disk
cv.imwrite(imageName,frame)
print('\n**File: "%s" is successfully written on disk at programs working directory**'%imageName)
print('\n>>Press \'Esc\' on Captured Image Window to close')
cv.waitKey(0)
cv.destroyWindow('Captured Image')
hd.mainhead('Thank You! Have a Nice Day')
#Release the Vision Source
visionSource.release()
