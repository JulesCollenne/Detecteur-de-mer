import numpy as np
from PIL import Image,ImageOps
import os, os.path


#
# Retourne un tableau d'images en format Image
# Les images sont contenues dans le dossier folder
# input : Nom du dossier contenant les images
#
def get_images(folder):
    imgs = []
    path = "/amuhome/c16009858/AA/"+folder
    valid_images = [".jpeg"]
    i = 0
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(Image.open(os.path.join(path, f)))
        i += 1
    return imgs

def resize_images(images):
    for i in range(len(images)):
        images[i] = images[i].resize((500, 500))
    return images

def image_to_array(images):
    i = 0
    for img in images:
        images[i] = np.array(img)
    return images

imgs_mer = resize_images(get_images("Mer"))
imgs_ailleurs = resize_images(get_images("Ailleurs"))

imgs_ailleurs[0].show()