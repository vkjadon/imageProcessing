import cv2 as cv
import numpy as np
import headers as hd

hd.mainhead('Program: Background Subtraction')
print('\nAction Required is represented by: >>')
hd.mainhead('Activities')
#Background Image
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Background Subtraction(Background) Case 3.png"

#Reading the Background Image
image=cv.imread(imagePath)

#Window Creation for displaying with different view options
cv.namedWindow('Background',cv.WINDOW_KEEPRATIO)
cv.imshow('Background',image)

#Conversion of Colorspace
image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

print('\n**Background Image Window is successfully generated**')
hd.subhead('Gray Background Matrix')
print(image)

#Foreground Image
imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Image Subtraction Understanding Case 3.png"
#imagePathF="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Matrix Understanding Case 1.png"

#Reading the Foreground Image
imageF=cv.imread(imagePathF)
cv.namedWindow('Foreground Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Foreground Image',imageF)

#Conversion of Colorspace
imageF=cv.cvtColor(imageF,cv.COLOR_BGR2GRAY)
print('\n**Foreground Image Window is successfully generated**')
hd.subhead('Gray Foreground Matrix')
print(imageF)

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
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')
