import numpy as np 
import os 
import cv2 as cv
from matplotlib import pyplot as plt
from processing.utils import *


def distance_map(edges_img):
    inverted_edges = 255 - edges_img
    dist = cv.distanceTransform(inverted_edges, cv.DIST_L2, 3)
    cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)
    return dist
