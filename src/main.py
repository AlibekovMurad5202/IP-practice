import sys
import argparse
import cv2 as cv
import converter

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

    image_HSV = converter.BGR2HSV(image)
    image_BGR = converter.HSV2BGR(image_HSV)
    cv.imshow("Image", image_BGR)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_hsv = converter.bgr2hsv(image)
    image_bgr = converter.HSV2BGR(image_hsv)
    cv.imshow("Image", image_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_hsv = converter.BGR2HSV(image)
    image_bgr = converter.hsv2bgr(image_hsv)
    cv.imshow("Image", image_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_bgr = converter.brightness_bgr(image, 100)
    cv.imshow("Image", image_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows()

    image_hsv = converter.BGR2HSV(image)
    image_2 = converter.brightness_hsv(image_hsv, 50)
    image_bgr = converter.HSV2BGR(image_2)
    cv.imshow("Image", image_bgr)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main() or 0)