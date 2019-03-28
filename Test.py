# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np

import cv2 as cv

import Images.image_save as imsa
import Images.ImageModifier as im
import Reader as re
from os import listdir
from os.path import isfile, join

#Permet d'obtenir les contours d'une image (problème : l'image est affichée à l'envers)
#Voir comment obtenir les vecteurs correspondants ()


#img = cv.imread('Data/Mer/qqqqq.jpeg',0)
#img = cv.resize(img, (500,500))

#sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)

#print (sobelx.shape)
#print(sobelx.flatten().shape)
#sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)


#plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
#plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
#plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
#plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#plt.show()

#
# Retourne les gradients des images mises en taille img_width x img_hight et les étiquettes
#
DataShape = (200,200)

def dataSobelY(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
   # print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
        data.append(sobely.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
        data.append(sobely.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target


def dataSobelX(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
   # print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        data.append(sobelx.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        data.append(sobely.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
  

    return data,target

def dataSobel (dirpath):
    data=[]
    target=[]
    
    seaPath = dirpath+"/Mer/"
    otherPath = dirpath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
   # print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobel = np.concatenate((sobelx,sobely),axis = 1)
        data.append(sobel.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobel = np.concatenate((sobelx,sobely),axis = 1)
        data.append(sobel.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
  

    return data,target

def SobelImage(dirPath):
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
   # print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,1)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobel = np.concatenate((sobelx,sobely),axis = 1)
        d = np.concatenate((sobel,img),axis = 1)
        data.append(d.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,1)
        img = cv.resize(img, DataShape)
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        d = np.concatenate((sobel,img),axis = 1)
        data.append(d.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
  

    return data,target
    
#data, target = dataSobel ("Data")
#print(data.shape)
#print(target.shape)

def getDataImage(dirPath):
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,1)
        img = cv.resize(img, DataShape)
        data.append(img.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,1)
        img = cv.resize(img, DataShape)
        data.append(img.flatten())
        target.append(-1)


    data=np.asarray(data)
    target=np.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target

def dataConcat (dirPath):
    dataS, targetS = dataSobelY(dirPath)
    dataC, targetC = getDataImage(dirPath)
    data = np.concatenate((dataS,dataC),axis=1)
    target = np.concatenate((targetS,targetC))
    return data, target


def createMirrorImages(dirPath): 
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,1)
        img = cv.flip(img,1)
        cv.imwrite( img_path+"Mirr.jpeg", img );

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,1)
        img = cv.flip(img,1)
        cv.imwrite( img_path+"Mirr.jpeg", img );
        
#createMirrorImages("Data")