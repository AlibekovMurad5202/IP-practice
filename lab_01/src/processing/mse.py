import cv2 as cv
import numpy as np

def mse(img1, img2):
    epsilon = 1e-10
    error = np.mean((np.float32(cv.absdiff(img1, img2))) ** 2)
    if error < epsilon:
        return 0
    else:
        return error