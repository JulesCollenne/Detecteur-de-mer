import sys
from PIL import Image

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

######################To_Execute######################
'''
#Ouverture du fichier image
ImageFile = '../Data/Mer/aaaaa.jpeg'
try:
  img = Image.open(ImageFile)
except IOError:
  print('Erreur sur ouverture du fichier ' + ImageFile)
  sys.exit(1)
#Affichage des caractéristiques de l'image
print(img.format,img.size, img.mode)

#Recupère les % RGB d'une image dans un vecteur (R,G,B)
vec = getColorRates(img)
print("R: "+str(vec[0])+" G: "+str(vec[1])+" B: "+str(vec[2]))

# fermeture du fichier image
img.close()
'''
######################To_Execute######################
