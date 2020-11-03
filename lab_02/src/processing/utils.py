import numpy as np
import cv2 as cv
import math
import matplotlib.pyplot as plt

def clamp_bgr_pixel(colors, value):
    b_result = max(min(colors[0] + value, 255), 0)
    g_result = max(min(colors[1] + value, 255), 0)
    r_result = max(min(colors[2] + value, 255), 0)
    return (b_result, g_result, r_result)

def MSE(img1, img2):
   h, w = img1.shape[:2]
   img2 = cv.resize(img2, (w, h))
   mse = np.mean((np.float32(cv.absdiff(img1, img2))) ** 2)
   return mse

def PSNR(img1, img2):
   epsilon = 1e-10
   mse = MSE(img1, img2)
   if mse < epsilon:
       return 0
   else:
        psnr = 10.0 * np.log10((255.0 * 255.0) / mse)
        return psnr

def intensity(bgr_color):
   return np.dot(bgr_color, [0.11, 0.59, 0.3])

def random_normal(mean, var, shape):
    gaussian = np.zeros(shape=shape, dtype='int16')
    gaussian = gaussian.reshape(-1)
    odd = False
    rng = np.random.RandomState()
    if len(gaussian) % 2 == 1:
        odd = True
    half = len(gaussian) // 2

    u1s, u2s = rng.uniform(size=half + 1), rng.uniform(size=half + 1)
    ss = -np.log(u1s)
    thetas = 2 * math.pi * u2s
    rs = np.sqrt(2 * ss) * var
    xs, ys = rs*np.cos(thetas) + mean, rs*np.sin(thetas) + mean

    for i in range(0, half):
        gaussian[2 * i] = xs[i]
        gaussian[2 * i + 1] = ys[i]
    if odd:
        gaussian[-1] = xs[-1]
    gaussian = gaussian.reshape(shape)
    return gaussian

def view_histogram(image, title):
    b_hist = np.zeros(shape=(256,), dtype=int)
    g_hist = np.zeros(shape=(256,), dtype=int)
    r_hist = np.zeros(shape=(256,), dtype=int)
    h, w, _ = image.shape
    for y in range(h):
        for x in range(w):
            b_hist[image[y, x][0]] += 1
            g_hist[image[y, x][1]] += 1
            r_hist[image[y, x][2]] += 1
    fig, ax = plt.subplots()
    ax.plot(range(0, 256), r_hist, color='r')
    ax.plot(range(0, 256), g_hist, color='g')
    ax.plot(range(0, 256), b_hist, color='b')
    ax.set_title(title)
    plt.show()
