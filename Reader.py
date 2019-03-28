from os import listdir
from os.path import isfile, join
import Images.Histogramme as Hi
import numpy
import Images.ColorRates as Cr
from PIL import Image



def dataHistogramme(dirPath):
    
    data=[]
    target=[]
    GlobalImgOrder=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    #print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        GlobalImgOrder.append(img_path)
        data.append(Hi.VectorHistogrammeC(img_path))
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        GlobalImgOrder.append(img_path)
        img_path = ""+otherPath+otherFileList[iOther]
        data.append(Hi.VectorHistogrammeC(img_path))
        target.append(-1)

    data=numpy.asarray(data)
    target=numpy.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target,GlobalImgOrder


def dataColorRates(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    #print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = ""+ seaPath + seaFileList[iSea]
        data.append(Cr.getColorRates(img_path))
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        img_path = ""+otherPath+otherFileList[iOther]
        data.append(Cr.getColorRates(img_path))
        target.append(-1)

    data=numpy.asarray(data)
    target=numpy.asarray(target)
    #print(data.shape)
    #print(target.shape)

    return data,target

