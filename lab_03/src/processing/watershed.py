import cv2 as cv
import numpy as np
import random as rng
from utils import *
from processing.canny import *

rng.seed(3818061)

def watershed(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges_img = canny_alg(gray).astype('uint8')
    inverted_edges = 255 - edges_img
    dist = cv.distanceTransform(inverted_edges, cv.DIST_L2, 3)
    cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)
    _, dist = cv.threshold(dist, 0.12, 1.0, cv.THRESH_BINARY)
    dist_8u = dist.astype('uint8')
    contours, _ = cv.findContours(dist_8u, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    markers = np.zeros(dist.shape, dtype=np.int32)

    for i in range(len(contours)):
        cv.drawContours(markers, contours, i, (i+1), -1)

    cv.circle(markers, (5,5), 3, (255,255,255), -1)
    cv.watershed(image, markers)
    mark = markers.astype('uint8')
    mark = cv.bitwise_not(mark)
    colors = []

    for contour in contours:
        colors.append((rng.randint(0,256), rng.randint(0,256), rng.randint(0,256)))

    dst = np.zeros((markers.shape[0], markers.shape[1], 3), dtype=np.uint8)

    for i in range(markers.shape[0]):
        for j in range(markers.shape[1]):
            index = markers[i,j]
            if index > 0 and index <= len(contours):
                dst[i,j,:] = colors[index-1]
    return dst
