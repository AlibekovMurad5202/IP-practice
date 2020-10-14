import cv2 as cv
import numpy as np
from processing.utils import *

def BGR2GRAY(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def bgr2gray(image):
    return np.uint8(np.dot(image, [0.07, 0.72, 0.21])
