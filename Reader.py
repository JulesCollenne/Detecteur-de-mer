from os import listdir
from os.path import isfile, join
import Histogramme as Hi

def dataHistogramme(dirPath):
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    data=[]
    target=[]
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    for iSea in range(0,len(seaFileList)-1):
        data.append(Hi.VectorHistogrammeC(seaFileList[iSea]))
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        data.append(Hi.VectorHistogrammeC(otherFileList[iOther]))
        target.append(-1)

    return data,target

