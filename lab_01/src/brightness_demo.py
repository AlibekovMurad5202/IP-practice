import sys
import argparse
from time import perf_counter
from processing.brightness_increase import *
from processing.color_models_converters import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image', 
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def brightness_increase(image):
    start = perf_counter()
    image_after = brightness_bgr(image, 150)
    finish = perf_counter()
    processing_time_BGR = finish - start
    cv.imshow("Image (BGR) (brightness += 150)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = bgr2YCrCb(image)
    start = perf_counter()
    image_bright = brightness_YCrCb(image_conv, 150)
    finish = perf_counter()
    processing_time_YCrCb = finish - start
    image_after = YCrCb2bgr(image_bright)
    cv.imshow("Image (YCrCb) (brightness += 150)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    return (processing_time_BGR, processing_time_YCrCb)

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    time_BGR, time_YCrCb = brightness_increase(image)
    print("time_BGR: {}".format(time_BGR))
    print("time_YCrCb: {}".format(time_YCrCb))

if __name__ == '__main__':
    sys.exit(main() or 0)
