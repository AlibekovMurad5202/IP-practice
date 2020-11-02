import numpy as np
import cv2 as cv
from processing.utils import *

def calculate_gaussian_kernel(radius: int, sigma: float):
    size = int(2 * radius + 1)
    values_range = range(-radius, radius + 1)
    grid = np.array([[i * i + j * j for i in values_range] for j in values_range])
    np.transpose(grid)
    kernel = np.exp(-grid / (2.0 * sigma * sigma))
    kernel = kernel / np.sum(kernel)
    return kernel

def calculate_pixel_color(image, x: int, y: int, kernel, radius: int):
    new_color = np.array([0, 0, 0])
    h, w, c = image.shape
    values_range = range(-radius, radius + 1)
    for j in values_range:
        for i in values_range:
            curr_color = image[max(min(y + i, h - 1), 0)][max(min(x + j, w - 1), 0)]
            new_color = new_color + curr_color * kernel[j + radius][i + radius]
    return clamp_bgr_pixel(new_color, 0)

def gauss_denoising(image, radius: int, sigma: float):
    kernel = calculate_gaussian_kernel(radius, sigma)
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            result_image[y, x] = calculate_pixel_color(image, x, y, kernel, radius)
    return result_image

def GAUSS_DENOISING(image, radius: int):
    result_image = cv.GaussianBlur(image, (radius, radius), 0)
    return result_image

