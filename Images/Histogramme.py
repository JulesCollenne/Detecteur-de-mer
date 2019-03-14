import cv2
import numpy as np
from matplotlib import pyplot as plt
image_list = []
from PIL import Image

# @param image, chemin de l'image.
# @return un vecteur de taille 768 (256*3)
# representant l'histogramme de couleur RGB succesivement
def VectorHistogrammeC(image_path):
    chans = cv2.split(cv2.imread(image_path))
    img = Image.open(image_path)
    x,y = img.size
    colors = ('b','g','r')
    features = []

    for (chan, color) in zip(chans, colors):
        	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        	features.extend(hist.flatten())
    return np.array(features).flatten()/(x*y)
