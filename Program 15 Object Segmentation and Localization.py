import headers as hd
import cv2 as cv
import numpy as np

#Function for finding centroid of object in image matrix
def Centroid(obj):
    row,col=obj.shape
    obj=np.matrix(obj)
    sumCols=np.matrix(np.sum(obj,0))
    colNum=np.matrix(np.arange(1,col+1,1))
    colMultiply=np.multiply(sumCols,colNum)
    total=np.sum(colMultiply)
    totalMatrix=np.sum(np.sum(obj))
    colLocation=int(total/totalMatrix)

    sumRows=np.matrix(np.sum(obj,1))
    sumRows=sumRows.transpose()
    rowNum=np.matrix(np.arange(1,row+1,1))
    rowMultiply=np.multiply(sumRows,rowNum)
    total=np.sum(rowMultiply)
    totalMatrix=np.sum(np.sum(obj))
    rowLocation=int(total/totalMatrix)

    return (rowLocation,colLocation)

hd.mainhead('Program: Object Segmentation and Localization')
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
print('\n>>Press \'B\' key on any Image to generate Subtracted Image Result<<')
while True:
    ret,frame1=visionSource.read()
    grayImageFg=cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
    cv.imshow('Foreground Image(LIVE)',frame1)
    k=cv.waitKey(5)
    if(k==66 or k==98):
        break
cv.destroyWindow('Foreground Image(LIVE)')
cv.imshow('Foreground Image',frame1)

#Difference
Difference=np.absolute(np.int16(grayImageFg)-np.int16(grayImageBg))
Difference[Difference>255]=255
Difference=np.uint8(Difference)
cv.imshow('Background Subtracted Image',Difference)
print('\n**Background Subtracted Image Window is successfully generated**')

#Thresholding 
blkWhite=Difference
thresholdValue=30
blkWhite[blkWhite<=thresholdValue]=0
blkWhite[blkWhite>thresholdValue]=255
bkWhite=np.uint8(blkWhite)
cv.imshow('Thresholded Image',blkWhite)

#Noise Removal
mask=np.ones((3,3),np.uint8)
noiseRemoval=cv.morphologyEx(blkWhite,cv.MORPH_OPEN,mask)
cv.imshow('Noise Removed Image',noiseRemoval)

#Object Labeling
ret,labels=cv.connectedComponents(noiseRemoval,4)
labelMatrix=np.matrix(labels)
i=1
objectMatList=[]
centroidList=[]
while(i<=np.amax(labels) and i<10):
    obj=labelMatrix==i       
    obj=np.uint8(obj)
    obj[obj>0]=255
    cv.imshow('Object'+str(i),obj)
    objectMatList.append(obj)   #Storing segmented objects
    centroid=Centroid(obj)      #function Call
    centroidList.append(centroid)   #Storing centroids of the objects
    cv.putText(frame1,str(i),(centroid[1],centroid[0]),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0))
    i=i+1
print('\n**Segmented Object Windows are successfully generated**')
hd.subhead('Object Centroids are tabulated below')
hd.mainhead('Table: Centroid of Objects')
print('Centroid Column represents (Index of Row,Index of Column) which specifies centroid of object in image matrix')
print('-'*53)
print('Objects','\t\t\t\t',' Centroid')
print('-'*53)
for index in range(0,len(objectMatList)):
    print('Object '+str(index+1),'\t\t\t\t',centroidList[index])
cv.imshow('Objects with Labels',frame1)
print('\n>>Press \'E\' key on any Image Window to close all Windows<<')
cv.waitKey(0)
cv.destroyAllWindows()
print('\n**Image Windows are successfully closed**')
hd.mainhead('Thank You!! Have a Nice Day!!')
