import numpy as np
from utils import *

def brightness_bgr(image, value):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            result_image[y, x] = clamp_bgr_pixel(image[y, x], value)
    return result_image

def brightness_YCrCb(image, value):
    height, width = image.shape[:2]
    result_image = image
    for y in range(height):
        for x in range(width):
            result_image[y, x, 0] = max(min(image[y, x, 0] + value, 255), 0)
    return result_image