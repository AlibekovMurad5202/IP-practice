import sys
import argparse
from time import perf_counter
from processing.watershed import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image', 
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def apply_watershed(image):
    start = perf_counter()
    dist = watershed(image)
    finish = perf_counter()
    processing_time_watershed = finish - start
    cv.imshow("Watershed", dist)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return processing_time_watershed

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0], cv.IMREAD_UNCHANGED)
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    processing_time = apply_watershed(image)
    print("time: {}".format(processing_time))
    
if __name__ == '__main__':
    sys.exit(main() or 0)
