import sys
import argparse
from demo.color_models_demo import *
from demo.brightness_demo import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to data', 
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])

    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    color_models_converting(image)
    time_BGR, time_YCrCb = brightness_increasing(image)
    print("time_BGR: {}".format(time_BGR))
    print("time_YCrCb: {}".format(time_YCrCb))

if __name__ == '__main__':
    sys.exit(main() or 0)