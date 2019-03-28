import os
import os.path

import numpy as np
from PIL import Image, ImageOps
import cv2

IMG_l = 500
IMG_L = 500
IMG_SIZE = (IMG_l, IMG_L)


#
# Retourne un tableau d'images en format Image
# Les images sont contenues dans le dossier folder
# input : Nom du dossier contenant les images
#
def get_images(folder):
    imgs = []
    path = "/amuhome/p18031960/Detecteur-de-mer/Data/" + folder
    valid_images = [".jpeg"]
    i = 0
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path, f)))
        i += 1
    return imgs


#
# Retourne le tableau d'images resizé en 500x500
# input : le tableau d'images
#
def resize_images(images):
    for i in range(len(images)):
        images[i] = images[i].resize(IMG_SIZE)
    return images


#
# Convertit les images du tableau images en npArray
# input : le tableau d'images
#
def image_to_array(images):
    i = 0
    for img in images:
        images[i] = np.array(img)
    return images


#
# Créé de nouvelles images à l'aide de modifications ( symétries, rotations etc... )
# input : le tableau d'images
#
def createll_new_images(images):
    for _ in images:
        images.append()
    return


def make_vector(images):
    new_images = np.zeros((len(images), IMG_l * IMG_L, 3))
    i = 0
    x = 0
    y = 0
    for img in images:
        new_images[i][:][:] = img[x][y][:]
        i += 1
    return new_images


def modificationsImage():
    #-----Reading the image-----------------------------------------------------
    img = cv2.imread('a.jpeg', 1)
    cv2.imshow("img",img) 
    
    #-----Converting image to LAB Color model----------------------------------- 
    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    cv2.imshow("lab",lab)
    
    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)
    cv2.imshow('l_channel', l)
    cv2.imshow('a_channel', a)
    cv2.imshow('b_channel', b)
    
    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    cv2.imshow('CLAHE output', cl)
    
    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))
    cv2.imshow('limg', limg)
    
    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    cv2.imshow('final', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# On récupère les images de type Image
#imgs_mer = resize_images(get_images("Mer"))
#imgs_ailleurs = resize_images(get_images("Ailleurs"))

#imgs_mer[0].show()

#imgs_mer = image_to_array(imgs_mer)

#print(imgs_mer[0][0][0][0], imgs_mer[0][0][0][1], imgs_mer[0][0][0][2])
