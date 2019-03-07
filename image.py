import numpy as np
from PIL import Image,ImageOps
import os, os.path
import cv2
import matplotlib.pyplot as plt

class image(object):

    def __init__(self):
        self.label = 0

#
# Retourne un tableau d'images en format np.array
# Les images sont contenues dans le dossier folder
# input : Nom du dossier contenant les images
#
def image_to_array(folder):
    imgs = []
    path = "/amuhome/c16009858/AA/"+folder
    valid_images = [".jpeg"]
    i = 0
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(np.array(Image.open(os.path.join(path, f))))
        i += 1
    return imgs


def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)


imgs_mer = image_to_array("Mer")
imgs_ailleurs = image_to_array("Ailleurs")

moyenne = np.zeros(imgs_mer[0].shape)
for i in imgs_mer:
    moyenne += i

moyenne /= len(imgs_mer)
moyenne_mer = moyenne


moyenne = np.zeros(imgs_ailleurs[0].shape)
for i in imgs_ailleurs:
    moyenne += i

moyenne /= len(imgs_ailleurs)
moyenne_ailleurs = moyenne

h = i.histogram()
l2 = h[256:512]
plt.figure(0)
for i in range(0, 256):
    plt.bar(i, l2[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)

plt.show()
