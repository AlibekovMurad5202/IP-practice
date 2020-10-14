import cv2 as cv
import numpy as np
from processing.utils import *

def BGR2GRAY(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def bgr2gray(image):
    result_image = (0.07 * image[:, :, 0] + 0.72 * image[:, :, 1] + 0.21 * image[:, :, 2]).astype(np.uint8)
    return result_image
