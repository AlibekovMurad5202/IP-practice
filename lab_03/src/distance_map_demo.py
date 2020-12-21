import sys
import argparse
from time import perf_counter
from processing.distance_map import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to edges image', 
        required = False, type = str, default = '../images/cup_edges.png', nargs = '+', dest = 'input')
    return parser

def get_distanse_map(image):
    start = perf_counter()
    dist = distance_map(image)
    finish = perf_counter()
    processing_time_dist = finish - start
    cv.imshow("Distance map", dist)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return processing_time_dist

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0], cv.IMREAD_UNCHANGED)
    cv.imshow("Edges image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    processing_time = get_distanse_map(image)
    print("time: {}".format(processing_time))
    
if __name__ == '__main__':
    sys.exit(main() or 0)
