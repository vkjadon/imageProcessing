import cv2 as cv
import numpy as np
import headers as hd

hd.mainhead('Program: Background Subtraction in Live Feed')
print('\nAction Required is represented by: >>')
hd.mainhead('Activities')
visionSource=cv.VideoCapture(1)
print('\n**Live Feed for Background Image Window is successfully generated**')
print('\n>>Press \'C\' on Live Feed Window to Capture the Background Image')
#Background Image
while True:
    ret,frame=visionSource.read()
    grayImageBg=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Background Image',frame)
    k=cv.waitKey(5)
    if(k==67 or k==99):
        break
#cv.destroyWindow('Background Image')
print('\n**Background Image is successfully captured**')

#Foreground Image
print('\n**Live Feed for Foreground Image Window is successfully generated**')
print('\n**Live Feed for Background Subtracted Image Window is successfully generated**')
print('\n>>Press \'B\' key on any Image to generate Subtracted Image Result<<')
while True:
    ret,frame1=visionSource.read()
    grayImageFg=cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    cv.imshow('Foreground Image(LIVE)',frame1)

    #Difference
    Difference=np.absolute(np.int16(grayImageFg)-np.int16(grayImageBg))
    Difference[Difference>255]=255
    Difference=np.uint8(Difference)
    cv.imshow('Background Subtracted Image(LIVE)',Difference)
    k=cv.waitKey(5)
    if(k==66 or k==98):
        break
cv.destroyWindow('Background Subtracted Image(LIVE)')
cv.destroyWindow('Foreground Image(LIVE)')
cv.imshow('Foreground Image',frame1)
cv.imshow('Backgound Subtracted Image',Difference)
print('\n**Background Subtracted Image Window is successfully generated**')
hd.subhead('Background Subtracted Image Matrix')
print(Difference)
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')
