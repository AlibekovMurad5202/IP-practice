from processing.utils import *

def gaussian_noise(image, mean, var):
    height, width = image.shape[:2]
    gaussian = np.random.normal(mean, var, (height, width)).astype('int16')
    noisy_image = np.zeros(shape=(height, width, 3), dtype='uint8')
    for y in range(height):
        for x in range(width):
            noisy_image[y, x,] = clamp_bgr_pixel(image[y, x], gaussian[y, x])
    return noisy_image
