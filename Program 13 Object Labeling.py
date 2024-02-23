import cv2 as cv
import numpy as np
import headers as hd

hd.mainhead('Program: Object Labeling')
print('\nAction Required is represented by: >>')
hd.mainhead('Activities')
#Background Image
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Object labeling Understanding (Background) Case 3.png"

#Reading the Background Image
image=cv.imread(imagePath)

#Window Creation for displaying with different view options
cv.namedWindow('Background',cv.WINDOW_KEEPRATIO)
cv.imshow('Background',image)
print('\n**Background Image Window is successfully generated**')

#Conversion of background image
image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Foreground Image
#imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 1.png"
#imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Matrix Understanding Case 1.png"
#imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Background Subtraction(Foreground) Case 4.png"
imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Object labeling Understanding Case 3.png"

#Reading the Foreground Image
imageF=cv.imread(imagePathF)
cv.namedWindow('Foreground Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Foreground Image',imageF)
print('\n**Foreground Image Window is successfully generated**')

#Conversion of Foreground Image
imageF=cv.cvtColor(imageF,cv.COLOR_BGR2GRAY)

#Difference
Difference=np.absolute(np.int16(imageF)-np.int16(image))
Difference[Difference>255]=255
Difference=np.uint8(Difference)
print('\n>>Press \'B\' key on any Image to generate Subtracted Image Result<<')
cv.waitKey(0)
cv.namedWindow('Backgound Subtracted Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Backgound Subtracted Image',Difference)
print('\n**Background Subtracted Image Window is successfully generated**')
hd.subhead('Background Subtracted Image Matrix')
print(Difference)
cv.waitKey(5)
#Thresholding
hd.subhead('User Input Required')
print('Note: Enter the minimum brightness value(other than 0) from subtracted matrix')
thValue=int(input('Enter the threshold value: '))
blackNwhite=Difference
blackNwhite[blackNwhite<thValue]=0
blackNwhite[blackNwhite>=thValue]=255
blackNwhite=np.uint8(blackNwhite)
print('\n>>Press \'T\' key on any Image to generate Thresholded Image Result<<')
cv.waitKey(0)
cv.namedWindow('Thresholded Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Thresholded Image',blackNwhite)
print('\n**Thresholded Image Window is successfully generated**')
hd.subhead('Thresholded Image Matrix')
print(blackNwhite)
'''
blackNwhite=cv.adaptiveThreshold(Difference,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,599,3)
cv.imshow('Thresholded Image',blackNwhite)
'''
#Object labeling
objects,labelMatrix=cv.connectedComponents(blackNwhite,4)
print('\n>>Press \'O\' key on any Image to generate Object label matrix<<')
cv.waitKey(0)
hd.subhead('Object label Matrix')
print(labelMatrix)
print('The number of objects present in field of view =',objects-1)
'''
print('\n>>Press \'V\' key on any Image to generate Isolated Object Images<<')
cv.waitKey(0)
#Isolation based on Label Matrix
#Object 1
object1=labelMatrix==1
object1=np.uint8(object1)
object1[object1>0]=255
cv.namedWindow('Object 1',cv.WINDOW_KEEPRATIO)
cv.imshow('Object 1',object1)
#Object 2
object2=labelMatrix==2
object2=np.uint8(object2)
object2[object2>0]=255
cv.namedWindow('Object 2',cv.WINDOW_KEEPRATIO)
cv.imshow('Object 2',object2)
#Object 3
object3=labelMatrix==3
object3=np.uint8(object3)
object3[object3>0]=255
cv.namedWindow('Object 3',cv.WINDOW_KEEPRATIO)
cv.imshow('Object 3',object3)
#If there are more objects in field of view then repeat the same 3 statements for all
print('\n**Object Image Windows are successfully generated**')
'''
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')
