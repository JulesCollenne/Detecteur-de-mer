import sys
from PIL import Image

#prend en argument le chemin d'une image et retourne son negatif
def negativeMode(path):
    img = Image.open(path)
    imgN = Image.new(img.mode, img.size)
    colonne, ligne = imgN.size
    for i in range(ligne):
        for j in range(colonne):
            pixel = img.getpixel((j,i))
            p = (255-pixel[0], 255-pixel[1], 255-pixel[2])
            imgN.putpixel((j,i),p)
    return imgN;
    import os;

#prend en argument le chemin d'une image et renvoi cette image dans sons sens inverse x->y => y->x
def miroir(path):
    img = Image.open(path)
    imgM = Image.new(img.mode, img.size)
    colonne, ligne = imgM.size
    for i in range(ligne):
        for j in range(colonne):
            pixel = img.getpixel((j,i))
            imgM.putpixel((colonne-j-1,i),pixel)
    return imgM;

#create nb rotated samples of the image img
def createRotatedSamples(img, nb):
    nbrotates=360/nb
    k=0
    r=0
    while(k<nb-1):
        r = r+nbrotates
        imgF = img.rotate(r, Image.BICUBIC, True)
        name = "hawkeye"+str(r)+".jpg"
        imgF.save('output/'+name)
        k=k+1

#Retourne un vecteur contenant les pourcentage RGB de l'image passé en argument
def getColorRates(img):
    column, line = img.size
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    for i in range(1):
        for j in range(10):
            pixel = img.getpixel((j,i))
            p1 = p1+pixel[0]
            p2 = p2+pixel[1]
            p3 = p3+pixel[2]

    p4 = p1+p2+p3
    per1 = int((p1/p4)*10000)/100
    per2 = int((p2/p4)*10000)/100
    per3 = int((p3/p4)*10000)/100
    return [per1, per2, per3]

#************************************************************************#

# ouverture du fichier image
ImageFile = './Data/Mer/aaaaa.jpeg'
try:
  img = Image.open(ImageFile)
except IOError:
  print('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)
# affichage des caractéristiques de l'image
print(img.format,img.size, img.mode)
# affichage de l'image
#img.show()

#negatif de l'Image
imgN = negativeMode(ImageFile)
#imgN.show()

#miroir de l'Image
#imgM = miroir(ImageFile)
#imgM.show()

#createRotatedSamples(imgN,20)

#recupère les % RGB d'une image
vec = getColorRates(img)
print("R: "+str(vec[0])+" G: "+str(vec[1])+" B: "+str(vec[2]))


# fermeture du fichier image
img.close()
