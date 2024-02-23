import headers as hd
import cv2 as cv
import numpy as np

hd.mainhead('Program: Object Centroid')
print('\nAction Required is represented by: >>')

#Specifying Image Path
imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image for Object Centroid Case 3.png"
#imagePath="D:\edu\Masters\Robotics and Humanoids\Vision\Python Programs\\Test Image with noise for Object Centroid Case 3.png"

#Reading the Image
image=cv.imread(imagePath)

#Showing the Image
cv.namedWindow('Read Image',cv.WINDOW_KEEPRATIO)
cv.imshow('Read Image',image)
#cv.destroyWindow('Read Image')

#Conversion into Grayscale
image_1D=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
hd.mainhead('Activities')
hd.subhead('Gray Image Matrix')
print(image_1D)

#Variable for rows and cols are initialized
hd.subhead('Shape of Image Matrix')
(rows,cols)=image_1D.shape
print('No. of Rows in Image: ',rows)
print('No. of Columns in Image: ',cols)

#Column Center of Brightness
hd.subhead('Finding Column Center of Brightness')
#Step-1: Sum the each column
sumCols=np.matrix(np.sum(image_1D,0))
print('\nStep a:Sum of Each Column:\n',sumCols)
#Step-2: Multiply the each column sum with its respective column no.(0,1,2,3.....n) 
colNum=np.matrix(np.arange(0,cols,1))
print('\nStep:Matrix for Column Indices:\n',colNum)
#Step-2a: Multiply both outpus from Step-1 and Step-2
colMultiply=np.multiply(sumCols,colNum)
print('\nStep b:Multiplication:\n',colMultiply)
#Step-3: Sum all the elements acquired from Step-2a
total=np.sum(colMultiply)
print('\nStep c:Total of multiplied matrix: ',total)
#Step-4: Total Sum of Matrix
totalMatrix=np.sum(image_1D)
#totalMatrix=np.sum(np.sum(image_1D))
print('\nStep d:Total of Image Matrix: ',totalMatrix)
#Step-5: Column Center=Step-3/Step-4
colCenter=total/totalMatrix
#colCenter=np.round(colLocation,0)
print('\nStep e:Column Center of Brightness: ',colCenter)

#Row Center of Brightness
hd.subhead('Finding Row Center of Brightness')
sumRows=np.matrix(np.sum(image_1D,1))
print('\nStep a:Sum of Each Row:\n',sumRows)
rowNum=np.matrix(np.arange(0,rows,1))
print('\nStep:Matrix for Row Indices:\n',rowNum)
rowMultiply=np.multiply(sumRows,rowNum)
print('\nStep b:Multiplication:\n',rowMultiply)
total=np.sum(rowMultiply)
print('\nStep c:Total of multiplied matrix: ',total)
totalMatrix=np.sum(image_1D)
print('\nStep d:Total of Image Matrix: ',totalMatrix)
rowCenter=total/totalMatrix
print('\nStep e:Row Center of Brightness: ',rowCenter)
#cv.putText(image,'1',(10,10),cv.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0))
print('\n>>Press \'P\' key on Image window to plot the center<<')
#Plotting Center
if(rows<100 and cols<100):
    #cv.circle(image,(int(colCenter),int(rowCenter)),1,(0,0,255),-1)
    #cv.circle(image,(int(rowCenter),int(colCenter)),1,(0,0,255),-1)
    cv.rectangle(image,(int(colCenter),int(rowCenter)),(int(colCenter),int(rowCenter)),(0,0,255),1)
else:
    #cv.rectangle(image,(int(colCenter),int(rowCenter)),(int(colCenter),int(rowCenter)),(0,0,255),1)
    cv.circle(image,(int(colCenter),int(rowCenter)),3,(0,0,255),-1)
#Plotted View
cv.waitKey(0)
cv.namedWindow('Object with Centroid',cv.WINDOW_KEEPRATIO)
cv.imshow('Object with Centroid',image)
print('\n**Plotted Image Window is successfully generated**')
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')

