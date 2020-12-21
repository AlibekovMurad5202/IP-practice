import sys
import argparse
from time import perf_counter
from processing.canny import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image', 
        required = True, type = str, nargs = '+', dest = 'input')
    return parser

def apply_canny(image):
    start = perf_counter()
    edges_img = canny_alg(image)
    finish = perf_counter()
    processing_time_canny = finish - start
    cv.imshow("Edges", edges_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return processing_time_canny

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0], 0)
    cv.imshow("Grayscale Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    processing_time = apply_canny(image)
    print("time: {}".format(processing_time))
    
if __name__ == '__main__':
    sys.exit(main() or 0)
