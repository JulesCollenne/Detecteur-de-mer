# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
2
import numpy as np
3
import cv2 as cv
4
5
img = cv.imread('Data/Ailleurs/ach.jpeg',0)
6
img= cv.GaussianBlur(img, (3, 3), 0)
7
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
8
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
9
10
pas=3
11
X = np.arange(0, img.shape[1], pas)
12
Y = np.arange(0, img.shape[0], pas)
13
U, V = np.meshgrid(X, Y)
14
gx=np.float32(sobelx)[0:img.shape[0]:pas,0:img.shape[1]:pas]
15
print (gx.shape)
16
print (U.shape)
17
gy=np.float32(sobely)[0:img.shape[0]:pas,0:img.shape[1]:pas]
18
fig, ax = plt.subplots()
19
q = ax.quiver(X, Y,gx , gy, scale=100000)
20
21
22
plt.show()