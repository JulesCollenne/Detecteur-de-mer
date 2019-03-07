#import glob
import cv2
import numpy as np
from matplotlib import pyplot as plt
image_list = []
'''
for filename in glob.glob('../Data/Mer/*.jpeg'):
    image_list.append(cv2.imread(filename))

chans = cv2.split(image_list[0])
colors = ('b','g','r')
features = []

for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist) 
	# plot the histogram
	plt.plot(hist, color = color)
	plt.xlim([0, 256])
dataImage=np.array(features).flatten()
print("flattened feature vector size: %d" % (dataImage.shape) )
print(dataImage)
'''

# @param image, chemin de l'image.
# @return un vecteur de taille 768 (256*3)
# representant l'histogramme de couleur RGB succesivement
def VectorHistogrammeC(image):
    chans = cv2.split(cv2.imread(image))
    colors = ('b','g','r')
    features = []

    for (chan, color) in zip(chans, colors):
        	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        	features.extend(hist) 
        	plt.plot(hist, color = color)
        	plt.xlim([0, 256])
    return np.array(features).flatten()
