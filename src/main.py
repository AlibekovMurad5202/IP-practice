import sys
import argparse
import cv2 as cv
import converter_2 as converter

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to data', required = True, type = str,
        nargs = '+', dest = 'input')
    return parser

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = converter.BGR2YCRCB(image)
    image_after = converter.YCRCB2BGR(image_conv)
    cv.imshow("Image (BGR -> YCRCB)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = converter.bgr2YCrCb(image)
    image_after = converter.YCRCB2BGR(image_conv)
    cv.imshow("Image (bgr -> YCRCB)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = converter.BGR2YCRCB(image)
    image_after = converter.YCrCb2bgr(image_conv)
    cv.imshow("Image (BGR -> YCrCb)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = converter.bgr2YCrCb(image)
    image_after = converter.YCrCb2bgr(image_conv)
    cv.imshow("Image (bgr -> YCrCb)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_after = converter.brightness_bgr(image, 150)
    cv.imshow("Image (BGR) (brightness += 150)", image_after)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_conv = converter.bgr2YCrCb(image)
    image_after = converter.brightness_YCrCb(image_conv, 150)
    image_bgr = converter.YCrCb2bgr(image_after)
    cv.imshow("Image (YCrCb) (brightness += 150)", image_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main() or 0)