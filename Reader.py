from os import listdir
from os.path import isfile, join
import Images.Histogramme as Hi
import numpy
from PIL import Image

def dataHistogramme(dirPath):
    
    data=[]
    target=[]
    
    seaPath = dirPath+"/Mer/"
    otherPath = dirPath+"/Ailleurs/"
    
    seaFileList = listdir(seaPath)
    otherFileList = listdir(otherPath)
    print(len(seaFileList))
    for iSea in range(0,len(seaFileList)-1):
        img_path = "../" + seaPath + seaFileList[iSea]
        img = Image.open(img_path)
        data.append(Hi.VectorHistogrammeC(img_path)/img.size)
        target.append(1)

    for iOther in range(0,len(otherFileList)-1):
        data.append(Hi.VectorHistogrammeC("../"+otherPath+otherFileList[iOther]))
        target.append(-1)

    data=numpy.asarray(data)
    target=numpy.asarray(target)
    print(data.shape)
    print(target.shape)

    return data,target