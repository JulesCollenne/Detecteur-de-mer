#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np

import cv2 as cv

import Images.image_save as imsa
from os import listdir
from os.path import isfile, join

DataShape = (200,200)

def getDataImage(dirPath):
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        data.append(img.flatten())
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        img = cv.imread(img_path,0)
        img = cv.resize(img, DataShape)
        data.append(img.flatten())
        target.append(-1)

    data=np.asarray(data)
    target=np.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target
    