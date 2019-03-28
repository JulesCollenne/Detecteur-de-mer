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

    return data,target,GlobalImgOrder


def dataHistogrammeCross(name_packets, target_packets):
    
    data=[ [] for line in range(len(name_packets)) ]
    target=[ [] for line in range(len(target_packets))]
    
    for p in range(len(name_packets)):
        for img in range(len(name_packets[p])):
            data[p].append(Hi.VectorHistogrammeC(name_packets[p][img]))
            target[p].append(target_packets[p][img])

    for line in range(len(name_packets)):
        data[line]=numpy.asarray(data[line])
        target[line]=numpy.asarray(target[line])

    return data,target

def dataColorRates(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    
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

    return data,target


def dataColorRatesCross(name_packets, target_packets):
    
    data=[ [] for line in range(len(name_packets)) ]
    target=[ [] for line in range(len(target_packets))]

    for p in range(len(name_packets)):
        for img in range(len(name_packets[p])):
            data[p].append(Cr.getColorRates(name_packets[p][img]))
            target[p].append(target_packets[p][img])
    
    for line in range(len(name_packets)):
        data[line]=numpy.asarray(data[line])
        target[line]=numpy.asarray(target[line])

    return data,target