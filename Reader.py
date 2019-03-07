from os import listdir
from os.path import isfile, join
import Histogramme as Hi
import numpy

def dataHistogramme(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    
    for iSea in range(0,len(seaFileList)-1):
        data.append(Hi.VectorHistogrammeC(seaFileList[iSea]))
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        data.append(Hi.VectorHistogrammeC(otherFileList[iOther]))
        target.append(-1)

    numpy.asarray(data)
    numpy.asarray(target)
    
    return data,target

