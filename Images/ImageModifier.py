import sys
import os
from PIL import Image
from math import sqrt
import time
import cv2 as cv

# @param objet Image
# @return objet Image
# Prend en argument une image et retourne la même image en negatif
def negative(img):
    imgN = Image.new(img.mode, img.size)
    column, line = imgN.size
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            p = (255-pixel[0], 255-pixel[1], 255-pixel[2])
            imgN.putpixel((j,i),p)
    return imgN;

# @param objet Image
# @return objet Image
# Prend en argument une image et renvoi cette image dans sons sens inverse x->y => y->x
def mirror(img):
    imgM = Image.new(img.mode, img.size)
    column, line = imgM.size
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            imgM.putpixel((column-j-1,i),pixel)
    return imgM;

# @param objet Image, nombre de nouvelles images, nom de dossier
# Prend l'image passé en argument, en créer nb copies ayant subit une rotation (écart de rotation proportionelle au nombre)
# et stock ces images dans le dossier voulu
def createRotatedSamples(img_path, nb, folder):
    img = Image.open(img_path)
    os.makedirs(folder, exist_ok=True)
    rotateMargin = 60
    nbrotates= rotateMargin/nb
    k=0
    r=0-rotateMargin/2
    while(k<nb-1):
        r = r+nbrotates
        imgF = img.rotate(r, Image.BICUBIC, True)
        name = "generated"+str(r)+".jpg"
        imgF.save(folder+'/'+name)
        k=k+1
        time.sleep(1)

# @param chemin d'une Image
# @return objet Image
# Prend en argument le chemin d'une image et créer l'équivalent de cette image en noir et blanc, puis la retourne.
def blackAndWhite(img_path):
    img = Image.open(img_path)
    imgN = Image.new(img.mode, img.size)
    column, line = imgN.size
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            pixelbw = int(pixel[0]/3+pixel[1]/3+pixel[2]/3)
            p = (pixelbw, pixelbw, pixelbw)
            imgN.putpixel((j,i),p)
    return imgN;

# @param objet Image, seuil
# @return objet Image
# Prend en argument une Image et un seuil, puis met en noir les pixels ayant des pixels voisin de couleur différentes
# en fonction du seuil donné
def shapeDetection(img_path, treshold):
    img = Image.open(img_path)
    imgS = Image.new(img.mode, img.size)
    column, line = imgS.size
    for i in range(1,line-1):
        for j in range(1,column-1):
            p1 = img.getpixel((j-1,i))
            p2 = img.getpixel((j,i-1))
            p3 = img.getpixel((j+1,i))
            p4 = img.getpixel((j,i+1))
            n = sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0]))
            if n < treshold:
                p = (255,255,255)
            else:
                p = (0,0,0)
            imgS.putpixel((j-1,i-1),p)
    return imgS;

##############################

def shapeDetectionCV(img, treshold):
    column = img.shape[0]
    line = img.shape[1]
    #print(img.shape)
    for i in range(1,line-1):
        for j in range(1,column-1):
            p1 = img[j-1][i]
            p2 = img[j][i-1]
            p3 = img[j+1][i]
            p4 = img[j][i+1]
            n = sqrt((p1-p3)*(p1-p3) + (p2-p4)*(p2-p4))
            if n < treshold:
                p = (255,255,255)
            else:
                p = (0,0,0)
            img[j-1][i-1] = p[0]
    return img;

#flatten
def flatten(img):
    column, line = img.size
    Vec=[]
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            #print(pixel[0])
            Vec.append(pixel[0])
            Vec.append(pixel[1])
            Vec.append(pixel[2])
    return Vec

##########################

def flattenCV(img):
    column, line = img.size
    Vec=[]
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            #print(pixel[0])
            Vec.append(pixel[0])
            Vec.append(pixel[1])
            Vec.append(pixel[2])
    return Vec
######################To_Execute######################
'''
#Ouverture du fichier image
ImageFile = '../Data/Mer/xlou.jpeg'
try:
  img = Image.open(ImageFile)
except IOError:
  print('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)

#Affichage l'image de base
#img.show()

#Negatif de l'Image
#imgN = negative(img)
#imgN.show()

#Miroir de l'Image
#imgM = mirror(img)
#imgM.show()

#Noir et blanc de l'image
#imgBW = blackAndWhite(ImageFile)
#imgBW.show()

#Detection de contours de l'image
#imgT = shapeDetection(ImageFile, 30)
#imgT.show()
#print(flatten(imgT))


#createRotatedSamples(ImageFile,10, "output")

#Fermeture du fichier image
img.close()
'''
######################To_Execute######################
