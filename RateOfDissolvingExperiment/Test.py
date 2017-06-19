import numpy as np
import cv2

img = cv2.imread('C:/Users/Laurel/PycharmProjects/RateOfDissolvingExperiment/download.jpg',-1)
cv2.imshow('image',img)
cv2.waitKey(0)
img = cv2.flip(img, 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()