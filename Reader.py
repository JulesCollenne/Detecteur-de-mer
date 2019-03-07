from os import listdir
from os.path import isfile, join
import Histogramme

def dataHistogramme(dirPath):
    seaPath = join(dirPath,"Mer\")
    otherPath = join(dirPath, "Ailleurs\")

    seaFileList = [f for f in listdir(seaPath) if isfile(join(dirPath, f))]
    otherFileList = [f for f in listdir(otherPath) if isfile(join(dirPath, f))]

    for iSea in range(0,len(seaFileList)-1):
        data.append(VectorHistogrammeC(seaFileList[i]))
        target.append(1)

    for iOther in range(0,len(seaFileList)-1)
        data.append(VectorHistogrammeC(otherFileList[i]))
        target.append(-1)

    return data,target

