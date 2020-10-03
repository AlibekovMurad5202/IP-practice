import numpy as np
import cv2 as cv
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i1', '--image1') #1st image path
    parser.add_argument('-i2', '--image2') #1st image path
    return parser

def PSNR(img1, img2):
   epsilon = 1e-10
   h, w = img1.shape[:2]
   img2 = cv.resize(img2, (w, h))
   tmp = cv.absdiff(img1, img2)
   tmp = np.float32(tmp)
   mse = np.mean( (np.float32(cv.absdiff(img1, img2))) ** 2)
   if mse < epsilon:
       return 0
   else:
        psnr = 10.0 * np.log10((255.0 * 255.0) / mse)
        return psnr


def main():
    parser = parse_args()
    args = parser.parse_args()
    img1 = cv.imread(args.image1)
    if img1 is None: 
        print("Incorrect 1st image path")
        sys.exit(1)
    img2 = cv.imread(args.image2)
    if img2 is None: 
        print("Incorrect 2nd image path")
        sys.exit(1)
    print(PSNR(img1, img2))

if __name__ == '__main__':
    main()