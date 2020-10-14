import sys
import argparse
from time import perf_counter
from processing.convert_to_grayscale import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image',
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def convert_to_grayscale(image):
    start = perf_counter()
    image_gray_cv = BGR2GRAY(image)
    finish = perf_counter()
    processing_time_cv = finish - start
    cv.imshow("Grayscale image using OpenCV conversion", image_gray_cv)
    cv.waitKey(0)
    cv.destroyAllWindows()

    start = perf_counter()
    image_gray_manual = bgr2gray(image)
    finish = perf_counter()
    processing_time_manual = finish - start
    cv.imshow("Grayscale image using luminosity conversion", image_gray_manual)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return processing_time_cv, processing_time_manual

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    time_cv, time_manual = convert_to_grayscale(image)

    print("time_CV: {}".format(time_cv))
    print("time_manual: {}".format(time_manual))


if __name__ == '__main__':
    sys.exit(main() or 0)