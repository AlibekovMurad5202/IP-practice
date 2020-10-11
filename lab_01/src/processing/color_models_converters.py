import cv2 as cv
import numpy as np
from processing.utils import clamp_bgr_pixel

def BGR2YCRCB(image):
    return cv.cvtColor(image, cv.COLOR_BGR2YCrCb)

def YCRCB2BGR(image):
    return cv.cvtColor(image, cv.COLOR_YCrCb2BGR)

def bgr2YCrCb_pixel(pixel, delta = None):
    delta = 128 if delta is None else delta
    y = pixel.dot([0.114, 0.587, 0.299])
    cr = (pixel[2] - y) * 0.713 + delta
    cb = (pixel[0] - y) * 0.564 + delta
    return (y, cr, cb)

def YCrCb2bgr_pixel(pixel, delta = None):
    delta = 128 if delta is None else delta
    y, cr, cb = pixel
    r = y + 1.403 * (cr - delta)
    g = y - 0.714 * (cr - delta) - 0.344 * (cb - delta)
    b = y + 1.773 * (cb - delta)
    return clamp_bgr_pixel((b, g, r), 0)

def bgr2YCrCb(image):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            result_image[y, x] = bgr2YCrCb_pixel(image[y, x], 128)
    return result_image

def YCrCb2bgr(image):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            result_image[y, x] = YCrCb2bgr_pixel(image[y, x], 128)
    return result_image
