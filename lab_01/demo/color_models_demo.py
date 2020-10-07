from converter import *

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