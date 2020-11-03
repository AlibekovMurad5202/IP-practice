import numpy as np
import cv2 as cv
from processing.utils import *

def calculate_pixel_color(image, x: int, y: int, radius: int):
    h, w, _ = image.shape
    values_range = range(-radius, radius + 1)
    min_color = max_color = image[y, x]
    for j in values_range:
        for i in values_range:
            curr_color = image[max(min(y + i, h - 1), 0)][max(min(x + j, w - 1), 0)]
            intensity_curr_color = np.dot(curr_color, [0.11, 0.59, 0.3])
            if intensity_curr_color > intensity(max_color):
                max_color = curr_color
            if intensity_curr_color < intensity(min_color):
                min_color = curr_color
    new_color = max_color / 2 + min_color / 2
    return clamp_bgr_pixel(new_color, 0)

def midpoint_filter_denoising(image, radius: int):
    height, width = image.shape[:2]
    result_image = np.copy(image)
    for y in range(height):
        for x in range(width):
            result_image[y, x] = calculate_pixel_color(result_image, x, y, radius)
    return result_image

