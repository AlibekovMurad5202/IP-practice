import numpy as np
import cv2
from processing.utils import *

def gaussian_noise(image, mean = 0, var = 100):
    height, width = image.shape[:2]
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (height, width)).astype('int16')
    noisy_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            noisy_image[y, x,] = clamp_bgr_pixel(image[y, x], gaussian[y, x])
    return noisy_image
