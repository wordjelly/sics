from skimage import graph, data, io, color, img_as_bool, segmentation, morphology, filters, img_as_float
from scipy import ndimage as ndi
from scipy import stats
from matplotlib import image as mimg
from matplotlib import pyplot as plt
from skimage import draw
import numpy as np
from skimage import io
import os
import cv2

from skimage.feature import canny
from skimage import measure
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter
from skimage.restoration import denoise_tv_chambolle, denoise_bilateral


img_name = 'sicst.jpg'
img = os.path.join(os.path.dirname(os.path.abspath(__file__)), img_name)
sics = io.imread(img)
edges = canny(sics[:,:,0])

selem = morphology.disk(6)
edges = morphology.dilation(edges, selem)


contours = measure.find_contours(edges,0.8)

fig,ax = plt.subplots(figsize=(4,3))

ax.imshow(edges,cmap=plt.cm.gray, interpolation='nearest')

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    print(contour)

plt.show()



"""
edges = canny(sics[:, :, 0])

fig, ax = plt.subplots(figsize=(4, 3))
canvas = fig.canvas

def onclick(event):
    ax.plot(event.xdata,event.ydata,'o')
    canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
ax.imshow(edges, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('Canny detector')


plt.show()



"""