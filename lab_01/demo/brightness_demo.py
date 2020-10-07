from time import perf_counter
from converter import *
from brightness import *

def brightness_increasing(image):
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