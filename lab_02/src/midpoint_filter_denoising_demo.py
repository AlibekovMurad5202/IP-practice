import sys
import argparse
from time import perf_counter
from processing.midpoint_filter_denoising import *
from processing.gauss_noise_generator import *

def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'Path to image', 
        required = True, type = str, nargs = '+', dest = 'input')
    parser.add_argument('-r', '--radius', help = 'Radius of gaussian kernel (default: 3)',
        required = False, type = int, default = 1, nargs = '?', dest = 'radius')
    parser.add_argument('-m', '--mean', help = 'Mean of gaussian distribution (default: 0)',
        required = False, type = float, default = 0.0, nargs = '?', dest = 'mean')
    parser.add_argument('-s', '--sigma', help = 'Standard deviation of gaussian distribution (default: 20)', 
        required = False, type = float, default = 20.0, nargs = '?', dest = 'sigma')
    return parser

def apply_midpoint_filter_denoising(image, radius, mean, sigma):
    noisy_image = gaussian_noise(image, mean, sigma)
    start = perf_counter()
    denoised_image = midpoint_filter_denoising(noisy_image, radius)
    finish = perf_counter()
    processing_time = finish - start

    cv.imshow("Noisy Image", noisy_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    view_histogram(image, "Histogram (Noisy Image)")

    cv.imshow("Filtered Image", denoised_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    view_histogram(image, "Histogram (Filtered Image)")

    affinity = [MSE(image, denoised_image), PSNR(image, denoised_image)]
    return (processing_time, affinity)

def main():
    args = build_argparser().parse_args()
    image = cv.imread(args.input[0])
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    view_histogram(image, "Histogram (Image)")

    processing_time, affinity = apply_midpoint_filter_denoising(image, args.radius, args.mean, args.sigma)
    print("time: {}".format(processing_time))
    print("MSE: {}".format(affinity[0]))
    print("PSNR: {}".format(affinity[1]))

if __name__ == '__main__':
    sys.exit(main() or 0)

