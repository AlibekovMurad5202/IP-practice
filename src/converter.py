import cv2 as cv
import numpy as np

def BGR2HSV(image):
    return cv.cvtColor(image, cv.COLOR_BGR2HSV)

def HSV2BGR(image):
    return cv.cvtColor(image, cv.COLOR_HSV2BGR)

def hue(r, g, b, max_value = None, min_value = None):
    max_value = max(r, g, b) if max_value is None else max_value
    min_value = min(r, g, b) if min_value is None else min_value
    delta = max_value - min_value
    if delta == 0:
        return 0
    h = 0
    if max_value == r:
        h = 60 * (g - b) / delta
    if max_value == g:
        h = 120 + 60 * (b - r) / delta
    if max_value == b:
        h = 240 + 60 * (r - g) / delta
    return h if h >= 0 else 360 + h

def saturation(r, g, b, max_value = None, min_value = None):
    max_value = max(r, g, b) if max_value is None else max_value
    min_value = min(r, g, b) if min_value is None else min_value
    return 0 if max_value == 0 else 255 * (1 - min_value / max_value)

def value(r, g, b, max_value = None, min_value = None):
    return max_value if max_value is not None else max(r, g, b)

def bgr2hsv(image):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            b = np.float32(image[y, x, 0])
            g = np.float32(image[y, x, 1])
            r = np.float32(image[y, x, 2])

            max_value = max(r, g, b)
            min_value = min(r, g, b)

            h = hue(r, g, b, max_value, min_value)
            s = saturation(r, g, b, max_value, min_value)
            v = value(r, g, b, max_value, min_value)

            result_image[y, x] = (h / 2, s, v)
    return result_image

def hsv2bgr_pixel(h, s, v):
    if s == 0:
        return (v, v, v)
    c = v * s / 255
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if h < 60:
        return (0 + m, x + m, c + m)
    elif h < 120:
        return (0 + m, c + m, x + m)
    elif h < 180:
        return (x + m, c + m, 0 + m)
    elif h < 240:
        return (c + m, x + m, 0 + m)
    elif h < 300:
        return (c + m, 0 + m, x + m)
    elif h < 360:
        return (x + m, 0 + m, c + m)

def hsv2bgr(image):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            h = np.float32(image[y, x, 0])
            s = np.float32(image[y, x, 1])
            v = np.float32(image[y, x, 2])
            result_image[y, x] = hsv2bgr_pixel(2 * h, s, v)
    return result_image

def clamp_pixel(colors, value):
    b_result = max(min(colors[0] + value, 255), 0)
    g_result = max(min(colors[1] + value, 255), 0)
    r_result = max(min(colors[2] + value, 255), 0)
    return (b_result, g_result, r_result)

def brightness_bgr(image, value):
    height, width = image.shape[:2]
    result_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            result_image[y, x] = clamp_pixel(image[y, x], value)
    return result_image

def brightness_hsv(image, value):
    height, width = image.shape[:2]
    result_image = image
    for y in range(height):
        for x in range(width):
            result_image[y, x, 2] = max(min(image[y, x, 2] + value, 255), 0)
    return result_image