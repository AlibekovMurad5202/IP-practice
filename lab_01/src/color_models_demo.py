import sys
import argparse
from processing.color_models_converters import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to data', 
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def color_models_converting(image):
    image_conv = BGR2YCRCB(image)
    image_after = YCRCB2BGR(image_conv)
    cv.imshow("Image (BGR -> YCRCB -> BGR)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = bgr2YCrCb(image)
    image_after = YCRCB2BGR(image_conv)
    cv.imshow("Image (bgr -> YCRCB -> BGR)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = BGR2YCRCB(image)
    image_after = YCrCb2bgr(image_conv)
    cv.imshow("Image (BGR -> YCrCb -> bgr)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = bgr2YCrCb(image)
    image_after = YCrCb2bgr(image_conv)
    cv.imshow("Image (bgr -> YCrCb -> bgr)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    color_models_converting(image)

if __name__ == '__main__':
    sys.exit(main() or 0)
