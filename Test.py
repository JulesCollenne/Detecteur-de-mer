# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np

import cv2 as cv

import Images.image_save as imsa
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
        img = cv.resize(img, (500,500))
        sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
        data.append(sobely.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, (500,500))
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
        img = cv.resize(img, (500,500))
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        data.append(sobely.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, (500,500))
        sobely = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
        data.append(sobely.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target

def dataSobel (dirpath):
    dataX, targetX = dataSobelX(dirpath)
    dataY, targetY = dataSobelY(dirpath)
    data = np.concatenate((dataX, dataY))
    target = np.concatenate((targetX,targetY))
    return data, target