import sys
import argparse
from time import perf_counter
from processing.gauss_noise_generator import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image', 
        required = True, type = str, nargs = '+', dest = 'input')
    parser.add_argument('-m', '--mean', help = 'Mean of gaussian distribution (default: 0)',
        required = False, type = int, default=0, nargs = '?', dest = 'mean')
    parser.add_argument('-v', '--var', help = 'Standard deviation of gaussian distribution (default: 20)', 
        required = False, type = int, default = 20, nargs = '?', dest = 'var')
    return parser

def apply_gaussian_noise(image, mean, var):
    start = perf_counter()
    noisy_image = gaussian_noise(image, mean, var)
    finish = perf_counter()
    processing_time_gauss = finish - start
    cv.imshow("Noisy Image", noisy_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    affinity = [MSE(image, noisy_image), PSNR(image, noisy_image)]
    return (processing_time_gauss, affinity)

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    processing_time, affinity = apply_gaussian_noise(image, args.mean, args.var)
    print("time: {}".format(processing_time))
    print("MSE: {}".format(affinity[0]))
    print("PSNR: {}".format(affinity[1]))
if __name__ == '__main__':
    sys.exit(main() or 0)