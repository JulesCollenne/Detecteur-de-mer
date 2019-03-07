import sys
import os
from PIL import Image

#prend en argument une image et retourne son negatif
def negative(img):
    imgN = Image.new(img.mode, img.size)
    column, line = imgN.size
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            p = (255-pixel[0], 255-pixel[1], 255-pixel[2])
            imgN.putpixel((j,i),p)
    return imgN;
    import os;

#prend en argument une image et renvoi cette image dans sons sens inverse x->y => y->x
def mirror(img):
    imgM = Image.new(img.mode, img.size)
    column, line = imgM.size
    for i in range(line):
        for j in range(column):
            pixel = img.getpixel((j,i))
            imgM.putpixel((column-j-1,i),pixel)
    return imgM;

#create nb rotated samples of the image img
def createRotatedSamples(img, nb, folder):
    os.makedirs(folder, exist_ok=True)
    nbrotates=360/nb
    k=0
    r=0
    while(k<nb-1):
        r = r+nbrotates
        imgF = img.rotate(r, Image.BICUBIC, True)
        name = "reroll"+str(r)+".jpg"
        imgF.save(folder+'/'+name)
        k=k+1

######################To_Execute######################

#Ouverture du fichier image
ImageFile = './Data/Mer/aaaaa.jpeg'
try:
  img = Image.open(ImageFile)
except IOError:
  print('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)

#Affichage l'image de base
img.show()

#Negatif de l'Image
imgN = negative(img)
imgN.show()

#Miroir de l'Image
imgM = mirror(img)
imgM.show()

createRotatedSamples(imgN,20, "generate")

#Fermeture du fichier image
img.close()

######################To_Execute######################
