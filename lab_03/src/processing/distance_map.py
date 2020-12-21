import cv2 as cv
import numpy as np

edges_img = cv.imread('lab_03/images/cup_edges.png', cv.IMREAD_UNCHANGED)
inverted_edges = 255 - edges_img

cv.imshow('Inverted binary Image', inverted_edges)
cv.waitKey(0)
cv.destroyAllWindows()

dist = cv.distanceTransform(inverted_edges, cv.DIST_L2, 3)

cv.normalize(dist, dist, 0, 1.0, cv.NORM_MINMAX)
cv.imshow('Distance Transform Image', dist)
cv.waitKey(0)
cv.destroyAllWindows()