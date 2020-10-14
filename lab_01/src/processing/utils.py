import numpy as np
import cv2 as cv

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